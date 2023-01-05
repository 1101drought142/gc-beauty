import { cartAddedFunc, counterFunc } from "./utils.js";
import publicAPI from "./api.js";

window.addEventListener('DOMContentLoaded', () => {
  counterFunc();
})

var acc = document.getElementsByClassName("product-drops__header");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function () {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
      this.classList.remove('active');
      panel.classList.remove('active');
    } else {
      this.classList.add('active');
      panel.classList.add('active');
      panel.style.maxHeight = panel.scrollHeight + 30 + "px";
    }
  });
}

var productSwiperThumb = new Swiper(".product-thumb-slider", {
  spaceBetween: 14,
  slidesPerView: 4,
  freeMode: true,
  watchSlidesProgress: true,
  navigation: {
    nextEl: ".product-thumb-slider__next",
    prevEl: ".product-thumb-slider__prev",
  },
});
var productSwiperMain = new Swiper(".product-slider", {
  spaceBetween: 10,
  thumbs: {
    swiper: productSwiperThumb,
  },
});

const addToFavoriteBtn = document.querySelector('.product__favorite');

addToFavoriteBtn.onclick = () => {
  const id = addToFavoriteBtn.closest('.product').getAttribute('data-id');
  publicAPI.addToFavorites(id).then(() => {
    addToFavoriteBtn.classList.add('active');
  })
}


const addProductBtn = document.querySelector('.product__add');

addProductBtn.onclick = () => {
  const count = document.querySelector('.counter-count').textContent.trim();
  const id = addProductBtn.closest('.product').getAttribute('data-id');
  publicAPI.addToCart(id, count).then(res => {
    cartAddedFunc();
  })
}


