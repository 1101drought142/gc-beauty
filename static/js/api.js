function is(className, object) {
  return Object.prototype.toString.call(object) === '[object '+ className +']';
}

class DataEncoder {
  constructor() {
    this.levels = [];
    this.actualKey = null;
    
  }
  __dataEncoding(data) {
    let uriPart = '';
    const levelsSize = this.levels.length;
    if (levelsSize) {
      uriPart = this.levels[0];
      for (let c = 1; c < levelsSize; c++) {
        uriPart += '[' + this.levels[c] + ']';
      }
    }
    let finalString = '';
    if (is('Object', data)) {
      const keys = Object.keys(data);
      const l = keys.length;
      for (let a = 0; a < l; a++) {
        const key = keys[a];
        let value = data[key];
        this.actualKey = key;
        this.levels.push(this.actualKey);
        finalString += this.__dataEncoding(value);
      }
    } else if (is('Array', data)) {
      if (!this.actualKey)
      throw new Error("Directly passed array does not work");
      const aSize = data.length;
      for (let b = 0; b < aSize; b++) {
        let aVal = data[b];
        this.levels.push(b);
        finalString += this.__dataEncoding(aVal);
      }
    } else {
      finalString += uriPart + '=' + encodeURIComponent(data) + '&';
    }
    this.levels.pop();
    return finalString;
  } 
  encode(data) {
    if (!is('Object', data) || data === {})
    return null;
    return this.__dataEncoding(data).slice(0, -1);
  }
}

class Api {
  constructor() {
    this.cartBaseApi = '/api/cart';
    this.favoritesBaseApi = '/api/favourites';
    this.catalogBaseApi = '/api/catalog';
  }

  addToCart = async (id, quantity) => {
    const url = `${this.cartBaseApi}/add/${id}/${quantity}/`;
    console.log(url);
    const res = await fetch(url);
    return await res;
  }
  deleteFromCart = async (id) => {
    const url = `${this.cartBaseApi}/delete/${id}/`;
    console.log(url);
    const res = await fetch(url);
    return await res;
  }
  changeCountCart = async (id, quantity) => {
    const url = `${this.cartBaseApi}/update/${id}/${quantity}`;
    console.log(url);
    const res = await fetch(url);
    return await res;
  }

  addToFavorites = async (id) => {
    const url = `${this.favoritesBaseApi}/add/${id}/`;
    console.log(url);
    const res = await fetch(url);
    return await res;
  }
  deleteFromFavorites = async (id) => {
    const url = `${this.favoritesBaseApi}/delete/${id}/`;
    console.log(url);
    const res = await fetch(url);
    return await res;
  }

  getCatalog = async (params) => {
    const encoder = new DataEncoder();
    const data = encoder.encode(params);
    const url = `${this.catalogBaseApi}/?${data}`;
    console.log(url);
    const res = await fetch(url);
    return await res.text();
  }

  search = async (string) => {
    const url = `/api/search_items/?search_string=${string}`;
    const res = await fetch(url);
    return await res.text();
  }

};

const publicAPI = new Api();

export default publicAPI;


