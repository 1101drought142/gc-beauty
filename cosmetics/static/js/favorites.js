import { cartAddedFunc } from './utils.js';
import publicAPI from './api.js';

const removeFromFavoritesBtns = document.querySelectorAll('.catalog-item__favorite');
removeFromFavoritesBtns.forEach(btn => {
  btn.onclick = (e) => {
    e.preventDefault();
    const item = btn.closest('.item-with-id')
    const id = item.getAttribute('id');

    publicAPI.deleteFromFavorites(id)
      .then(() => {
        item.remove();
      })
  }
})

const addToCartBtns = document.querySelectorAll('.favorites-item__cart');
addToCartBtns.forEach(btn => {
  btn.onclick = (e) => {
    e.preventDefault();
    const item = btn.closest('.item-with-id');
    const id = item.getAttribute('id');

    publicAPI.addToCart(id, 1)
      .then(() => {
        cartAddedFunc();
      })
  }
})

