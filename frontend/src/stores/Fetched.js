import { defineStore } from "pinia";

export const useFetchedStore = defineStore("fetchedStore", {
  state: () => ({
    dates: [],
    products: [],
    stores: [],
    transactions: [],
    name: "Jason",
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
  },
});
