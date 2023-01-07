from django.views.generic import TemplateView, View
from django.core.mail import send_mail
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db import IntegrityError, transaction
from .models import ItemCategories, Item, Certificates, Banners, Team, Photos, Tags, Types, CallbackForm, OrderItem, Order
from .session_stored_products import Cart_Session, Liked_Session
from .forms import ContactForm, OrderForm
from django.conf import settings


# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["catalog_items"] = Item.objects.all()
        context["home_banners"] = Banners.objects.all()
        context["categories"] = ItemCategories.objects.filter(father_categorie__isnull=True)
        context["show_more_button"] = True if context["catalog_items"].count() > 12 else False

        return context

class Company(TemplateView):
    template_name = "company.html"
    def get_context_data(self, *args, **kwargs):
        context = super(Company, self).get_context_data(*args, **kwargs)
        context["team"] = Team.objects.all()
        context["certificates"] = Certificates.objects.all()
        context["breadcrumbs"] = [["О бренде", "company"]]
        return context

class Catalog(TemplateView):
    template_name = "catalog.html"
    def get_context_data(self, *args, **kwargs):
        context = super(Catalog, self).get_context_data(*args, **kwargs)

        items_filter = {}
        if (kwargs.get("section_slug")):
            items_filter["father_categorie__slug"] = kwargs["section_slug"]
        else:
            items_filter = {}
        
        context["catalog_items"] = Item.objects.filter(**items_filter).order_by("sort")[:12]
        context["extra_js_links"] = ["/js/catalog.js"]
        context["categories"] = ItemCategories.objects.filter()
        context["types"] = Types.objects.filter()
        context["tags"] = Tags.objects.all()
        context["show_more_button"] = True if context["catalog_items"].count() > 12 else False
        return context

class CatalogItem(TemplateView):
    template_name = "product.html"
    def get_context_data(self, *args, **kwargs):
        context = super(CatalogItem, self).get_context_data(*args, **kwargs)
        context["item"] = get_object_or_404(Item, slug = kwargs["item_slug"])
        context["photos"] = Photos.objects.filter(item__slug = kwargs["item_slug"]) 
        context["extra_js_links"] = ["/js/product.js"]
        context["breadcrumbs"] = [["Каталог", "catalog"], [context["item"].name, context["item"].slug]]
        context["similar_items"] = context["item"].similar_items.all()
        return context

class Payment(TemplateView):
    template_name = "payment.html"
    def get_context_data(self, *args, **kwargs):
        context = super(Payment, self).get_context_data(*args, **kwargs)
        context["breadcrumbs"] = [["Оплата", "payment"]]
        context["footer_form"] = ContactForm()
        return context

class Shipping(TemplateView):
    template_name = "shipping.html"
    def get_context_data(self, *args, **kwargs):
        context = super(Shipping, self).get_context_data(*args, **kwargs)
        context["breadcrumbs"] = [["Доставка", "shipping"]]
        context["footer_form"] = ContactForm()
        return context

class Garantees(TemplateView):
    template_name = "garantees.html"
    def get_context_data(self, *args, **kwargs):
        context = super(Garantees, self).get_context_data(*args, **kwargs)
        context["breadcrumbs"] = [["Гарантии", "garantees"]]
        context["footer_form"] = ContactForm()
        return context

class Contacts(TemplateView):
    template_name = "contacts.html"
    def get_context_data(self, *args, **kwargs):
        context = super(Contacts, self).get_context_data(*args, **kwargs)
        context["breadcrumbs"] = [["Контакты", "contacts"]]
        context["footer_form"] = ContactForm()
        return context




class OrderTemplate(TemplateView):
    template_name = "offer.html"
    def get_context_data(self, *args, **kwargs):
        cart_content = Cart_Session(self.request)
        context = super(Order, self).get_context_data(*args, **kwargs)
        context["breadcrumbs"] = [["Оформление заказа", "order"]]
        context["catalog_items"] = cart_content.return_cart_contents()
        context["extra_js_links"] = ["/js/shared.js", "/js/offer.js"]
        context["price"] = cart_content.calc_price()
        context["footer_form"] = ContactForm()
        return context


class CreatedOrder(TemplateView):
    template_name = "created.html"


class CartApi:

    def add(request, id, quantity):
        try:
            Cart_Session(request).add(id, quantity)
            return HttpResponse("Sucsess")
        except:
            raise Http404

    def delete(request, id):
        try:
            Cart_Session(request).delete(id)
            return HttpResponse("Sucsess")
        except:
            raise Http404

    def update(request, id, quantity):
        try:
            Cart_Session(request).change_quantity(id, quantity)
            return HttpResponse("Sucsess")
        except:
            raise Http404


class BaseCart(TemplateView):
    def get_context_data(self, *args, **kwargs):
        cart_content = Cart_Session(self.request)
        context = super(BaseCart, self).get_context_data(*args, **kwargs)
        context["catalog_items"] = cart_content.return_cart_contents()
        context["price"] = cart_content.calc_price()
        return context

class Cart(BaseCart):
    template_name = "cart.html"
    def get_context_data(self, *args, **kwargs):
        context = super(Cart, self).get_context_data(*args, **kwargs)
        context["extra_js_links"] = ["/js/utils.js", "/js/cart.js"]
        
        context["breadcrumbs"] = [["Корзины", "cart"]]
        
        return context

class CartApiPage(BaseCart):
    template_name = "cart_page_content.html"
    
   

class LikedApi:
    def add(request, id):
        try:
            Liked_Session(request).add(id)
            return HttpResponse("Sucsess")
        except:
            raise Http404

    def delete(request, id):
        try:
            Liked_Session(request).delete(id)
            return HttpResponse("Sucsess")
        except:
            raise Http404

class LikedBase(TemplateView):
    def get_context_data(self, *args, **kwargs):
        cart_content = Liked_Session(self.request)
        context = super(LikedBase, self).get_context_data(*args, **kwargs)
        context["catalog_items"] = cart_content.return_cart_contents()
        return context


class Liked(LikedBase):
    template_name = "favourites.html"
    def get_context_data(self, *args, **kwargs):
        context = super(Liked, self).get_context_data(*args, **kwargs)
        context["breadcrumbs"] = [["Избранное", "favourites"]]
        context["extra_js_links"] = ["/js/favorites.js"]
        context["footer_form"] = ContactForm()
        return context

class LikedApiPage(LikedBase):
    template_name = "favourites_page_content.html"


class AjaxItems(TemplateView):
    
    template_name = "items.html"

    def get_context_data(self, *args, **kwargs):
        
        context = super(AjaxItems, self).get_context_data(*args, **kwargs)
        base_num = 12
        filter = {}
       
        if (self.request.GET.get("section")):
            if (self.request.GET.get("section") != "0" ):
                filter["father_categorie"] = self.request.GET.get("section")
            else:
                filter = {}

        if (self.request.GET.get("tags[0]")):
            c = 1
            temp_tags = [self.request.GET.get("tags[0]")]
            while self.request.GET.get("tags[" + str(c) + "]"):
                temp_tags.append(self.request.GET.get("tags[" + str(c) + "]"))
                c+=1
            filter["tags__in"] = temp_tags

        if (self.request.GET.get("type")):
            filter["types"] = self.request.GET.get("type")

        if (self.request.GET.get("page_num")):
            base_num += int(self.request.GET.get("page_num")) * 12

        context["catalog_items"] = Item.objects.filter(**filter).order_by("sort")[:base_num]
        
        return context

class AjaxSearch(TemplateView):
    template_name = "search.html"

    def get_context_data(self, *args, **kwargs):
        
        context = super(AjaxSearch, self).get_context_data(*args, **kwargs)
        if (self.request.GET.get("search_string")):
            context["catalog_items"] = Item.objects.filter(name__icontains=self.request.GET.get("search_string")).order_by("sort")

        return context

class FormResult(View):

    def post(self, request, *args, **kwargs):
        
        form = ContactForm(request.POST)
        
        if not(form.is_valid()):
            raise Http404

        try:

            with transaction.atomic():
                
                creted_object = CallbackForm.objects.create(name=form.cleaned_data["name"], phone=form.cleaned_data["phone"])

                message = f"{creted_object.created_time}\n{creted_object.name} {creted_object.phone}"

                send_mail(
                    f'Новая заявка от {creted_object.name}', 
                    message,
                    settings.DEFAULT_FROM_EMAIL, 
                    settings.RECIPIENTS_EMAIL
                )
                
                return render(request, "created.html",
                    {
                        "name" : creted_object.name,
                        "phone": creted_object.phone,
                        "date": creted_object.created_time,
                        "id": creted_object.pk
                    }
                )

        except Exception as e:
            raise Http404

class OrderResult(View):

    def post(self, request, *args, **kwargs):
        
        form = OrderForm(request.POST)

        cart_content = Cart_Session(request)
        in_cart_items = cart_content.return_cart_contents()
        

        
        if not(form.is_valid()) and in_cart_items:
            raise Http404
    
        print(form.is_valid())
        creted_object = Order.objects.create(
            name=form.cleaned_data["name"], 
            mail=form.cleaned_data["mail"],
            phone=form.cleaned_data["phone"],
            city=form.cleaned_data["city"],
            street=form.cleaned_data["street"],
            index=form.cleaned_data["index"],
            house=form.cleaned_data["house"],
            flat=form.cleaned_data["flat"],
            payment_type=form.cleaned_data["payment_type"],
            payed=False,
            total=cart_content.calc_price(),
        )
        order_items = []
        for key in in_cart_items:
            temp_item = get_object_or_404(Item, pk=key)
            order_item = OrderItem.objects.create(
                item=temp_item, 
                quantity=in_cart_items[key]["quantity"],
                order=creted_object,
            )
            order_items.append(order_item)

        
    

        message = f"{creted_object.created_time}\n"\
                f"Имя: {creted_object.name}\n"\
                f"Телефон: {creted_object.phone}\n"\
                f"Почта: {creted_object.mail}\n"\
                f"Адрес: {creted_object.city} {creted_object.street} {creted_object.house} {creted_object.flat} {creted_object.index}"\
                f"Способ оплаты : {creted_object.payment_type}\n\n\n"
        
        for item in order_items:
            message += f"{item.item.name}  {item.quantity}\n"
                    

        send_mail(
            f'Новый заказ от {creted_object.name}', 
            message,
            settings.DEFAULT_FROM_EMAIL, 
            settings.RECIPIENTS_EMAIL
        )
        
        return render(request, "created_order.html",
            {
                "name" : creted_object.name,
                "phone": creted_object.phone,
                "date": creted_object.created_time,
                "id": creted_object.pk,
                "mail": creted_object.mail,
                "adress": f"{creted_object.city}, {creted_object.street}, {creted_object.house}, {creted_object.flat}, {creted_object.index}",
                "payment": creted_object.payment_type,
            }
        )

        