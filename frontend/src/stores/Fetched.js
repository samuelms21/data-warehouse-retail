import { defineStore } from "pinia";

export const useFetchedStore = defineStore("fetchedStore", {
  state: () => ({
    dates: [],
    products: [],
    stores: [],
    transactions: [],
    qty_solds: [],
    total_sales: [],
  }),
  actions: {
    async callAPIs() {
      try {
        // dates
        const datesResponse = await fetch("http://127.0.0.1:5000/dates");
        this.dates = await datesResponse.json();

        // products
        const productsResponse = await fetch("http://127.0.0.1:5000/products");
        this.products = await productsResponse.json();

        // stores
        const storesResponse = await fetch("http://127.0.0.1:5000/stores");
        this.stores = await storesResponse.json();

        // transactions
        const transactionsResponse = await fetch(
          "http://127.0.0.1:5000/transactions"
        );
        this.transactions = await transactionsResponse.json();
      } catch (error) {
        console.error(error.message);
      }
    },
    async getQuantityOfItemsSold(dateId, storeId = null, productId = null) {
      // console.log(
      //   `WIII: ${dateId}, ${storeId}, ${productId ? productId : ""},`
      // );
      try {
        // dates
        const qtySoldsResponse = await fetch(
          `http://127.0.0.1:5000/qty_items_sold?group_by=store&date_id=${dateId}&store_id=${
            storeId ? storeId : ""
          }&product_id=${productId ? productId : ""}`
        );
        this.qty_solds = await qtySoldsResponse.json();
      } catch (error) {
        console.error(error.message);
      }
    },
  },
});
