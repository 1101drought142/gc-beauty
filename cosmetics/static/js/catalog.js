import publicAPI from "./api.js";

const openFilterBtn = document.querySelector('.catalog-filter__btn');
const filter = document.querySelector('.catalog-filter');

openFilterBtn.onclick = () => {
  filter.classList.toggle('active');
}


const filterBtns = document.querySelectorAll('.catalog-btns__item');

const wrap = document.querySelector('.catalog-wrap');
filterBtns.forEach(btn => {
  btn.onclick = () => {
    setTimeout(() => {
      const data = {
        'section': '',
        'types': '',
        'tags': '',
      };

      data['section'] = document.querySelector('.catalog-btns__input[name="section"]:checked').value;
      data['type'] = document.querySelector('.catalog-filter__input[name="type"]:checked')
        ? document.querySelector('.catalog-filter__input[name="type"]:checked').value
        : '';
      data['tags'] = [];
      const tags = document.querySelectorAll('.catalog-filter__input[name="tag"]:checked');
      if (tags.length < 1) {
        data['tags'] = '';
      };
      console.log(tags);
      tags.forEach(el => {
        data['tags'].push(el.value);
      })


      publicAPI.getCatalog(data).then(res => {
        wrap.innerHTML = res;
      })
    }, 100);
  }
})

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



