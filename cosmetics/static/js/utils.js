import publicAPI from "./api.js";

export function counterFunc() {
  const minuses = document.querySelectorAll('.counter-minus');
  const pluses = document.querySelectorAll('.counter-plus');

  minuses.forEach(btn => {
    btn.onclick = (e) => {
      e.preventDefault();
      const count = btn.closest('.counter').querySelector('.counter-count');
      count.textContent = +count.textContent > 1 ? +count.textContent - 1 : 1;

      const id = btn.closest('.item-with-id').getAttribute('id');
      publicAPI.changeCountCart(id, +count.textContent);
    }
  })
  pluses.forEach(btn => {
    btn.onclick = (e) => {
      e.preventDefault();
      const count = btn.closest('.counter').querySelector('.counter-count');
      count.textContent = +count.textContent < 99 ? +count.textContent + 1 : 99;
      
      const id = btn.closest('.item-with-id').getAttribute('id');
      publicAPI.changeCountCart(id, +count.textContent);
    }
  })
}

export function cartAddedFunc() {
  const plate = document.querySelector('.cart-added');
  plate.classList.add('active');
  setTimeout(() => {
    plate.classList.remove('active');
  }, 3500);
}

export function closeModals() {
  document.querySelector('.modal-bg').classList.remove('active');
  document.querySelectorAll('.overscreen').forEach(over => over.classList.remove('active'));
  document.querySelector('body').style.overflow = 'auto';
}
