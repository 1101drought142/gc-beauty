import publicAPI from "./api.js";
import { closeModals } from "./utils.js";

const body = document.querySelector('body');
const modalBg = document.querySelector('.modal-bg');

modalBg.onclick = () => {
  closeModals();
};

const burgerBtn = document.querySelector('.header__burger');
const burgerClose = document.querySelector('.burger-top__close');
const burgerMenu = document.querySelector('.burger');

burgerBtn.onclick = () => {
  burgerMenu.classList.add('active');
  modalBg.classList.add('active');
  body.style.overflow = 'hidden';
}
burgerClose.onclick = () => {
  closeModals();
}

const burgerSearch = document.querySelector('.burger-top-search__input');
const searchMenu = document.querySelector('.search-menu');

burgerSearch.oninput = (e) => {
  const value = e.target.value;
  if (value.length >= 2) {
    searchMenu.classList.add('active');
    publicAPI.search(value)
    .then((res) => {
      searchMenu.innerHTML = res;
    })
  } else {
    searchMenu.classList.remove('active');
  }
}

