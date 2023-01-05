import { counterFunc } from "./utils.js";
import publicAPI from "./api.js";


counterFunc();

const recalcFunc = () => {
  const items = document.querySelectorAll('.cart-item');

  items.forEach(item => {
    const count = +item.querySelector('.counter-count').textContent;
    const singlePrice = +item.querySelector('.single-price').textContent;

    const totalItemPrice = item.querySelector('.total-single-price');
    totalItemPrice.textContent = count * singlePrice;
  })

  const allTotalItemPrices = [];
  const allTotalItemPricesElements = document.querySelectorAll('.total-single-price');
  allTotalItemPricesElements.forEach(element => {
    allTotalItemPrices.push(+element.textContent);
  })

  const finalCartPrice = document.querySelector('.final-cart-price');
  finalCartPrice.textContent = allTotalItemPrices.reduce((a, b) => a + b, 0);
}

const allBtnsToRecalc = document.querySelectorAll('.click-to-recalc');
allBtnsToRecalc.forEach(btn => {
  btn.addEventListener('click', recalcFunc);
})


const deleteBtns = document.querySelectorAll('.cart-item__delete');
deleteBtns.forEach(btn => {
  btn.onclick = (e) => {
    e.preventDefault();
    const id = btn.closest('.cart-item').getAttribute('id');
    publicAPI.deleteFromCart(id);
    btn.closest('.cart-item').remove();
    recalcFunc();
  }
})

