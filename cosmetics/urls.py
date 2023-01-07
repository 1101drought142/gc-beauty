from . import views
from django.urls import path

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("company/", views.Company.as_view(), name="company"),
    
    path("catalog/", views.Catalog.as_view(), name="catalog"),
    path("catalog/<slug:section_slug>/", views.Catalog.as_view(), name="catalog_section"),
    path("catalog-item/<slug:item_slug>/", views.CatalogItem.as_view(), name="catalog_item"),
    
    path("cart/", views.Cart.as_view(), name="cart"),
    path("favourites/", views.Liked.as_view(), name="liked"),
    
    path("payment/", views.Payment.as_view(), name="payment"),
    path("shipping/", views.Shipping.as_view(), name="shipping"),
    path("garantees/", views.Garantees.as_view(), name="garantees"),
    path("contacts/", views.Contacts.as_view(), name="contacts"),

    path("order/", views.OrderTemplate.as_view(), name="order"),
    path("finish_order/", views.CreatedOrder.as_view(), name="finish_order"),
    
    

    path("api/catalog/", views.AjaxItems.as_view(), name="api_catalog"),
    
    path("api/cart/add/<int:id>/<int:quantity>/", views.CartApi.add, name="cart_add"),
    path("api/cart/delete/<int:id>/", views.CartApi.delete, name="cart_delete"),
    path("api/cart/update/<int:id>/<int:quantity>/", views.CartApi.update, name="cart_update"),
    path("api/cart/page_update/", views.CartApiPage.as_view(), name="cart_update_page"),

    path("api/favourites/add/<int:id>/", views.LikedApi.add, name="liked_add"),
    path("api/favourites/delete/<int:id>/", views.LikedApi.delete, name="liked_delete"),
    path("api/favourites/page_update/", views.LikedApiPage.as_view(), name="liked_update_page"),

    path("api/search_items/", views.AjaxSearch.as_view(), name="ajax_search"),
    path("api/contact_form/", views.FormResult.as_view(), name="ajax_search"),
    path("api/order_form/", views.OrderResult.as_view(), name="ajax_search"),
    
]
