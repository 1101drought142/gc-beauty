import publicAPI from "./api.js";

const swiper = new Swiper('.hero-swiper', {
  loop: true,

  pagination: {
    el: '.hero-swiper__pagination',
  },
});


const filterBtns = document.querySelectorAll('.catalog-btns__item');
const wrap = document.querySelector('.catalog-wrap');

filterBtns.forEach(btn => [
  btn.onclick = () => {
    setTimeout(() => {
      const category = document.querySelector('.catalog-btns__input:checked').getAttribute('data-category');
      const data = {
        'section': category
      };

      publicAPI.getCatalog(data).then(res => {
        wrap.innerHTML = res;
      })
    }, 100);
  }
])

const addToFavoriteBtns = document.querySelectorAll('.catalog-item__favorite');

addToFavoriteBtns.forEach(btn => {
  btn.onclick = (e) => {
    e.preventDefault();
    const id = btn.closest('.catalog-item').getAttribute('data-id');
    publicAPI.addToFavorites(id).then(() => {
      btn.classList.add('active');
    })
  }
});

try {
  const preloader = document.querySelector('.preloader');

  console.log(window.localStorage.getItem('loaded'));
  console.log(window.localStorage.getItem('loaded') == 1);
  if (window.localStorage.getItem('loaded') == 1) {
    preloader.style.display = 'none';
  } else {
    preloader.style.opacity = '1';
  }

  const preloaderFunc = () => {
    setTimeout(() => {
      preloader.classList.add('loaded');
      window.localStorage.setItem('loaded', 1);
      const spans = document.querySelectorAll('.hero__title.hero__title-anim span');
      spans.forEach(anim => {
        anim.classList.add('active');
      });
    }, 5500);
  }
  preloaderFunc();
} catch (e) {
  console.log(e);
}
