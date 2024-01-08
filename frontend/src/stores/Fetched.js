import { defineStore } from "pinia";

export const useFetchedStore = defineStore("fetchedStore", {
    state: () => ({
        dates: [],
        products: [],
        stores: [],
        transactions: [],
        qty_solds: [],
        gross_profits: [],
        gross_margins: [],
        dateInitIndex: 28,
        apiErrorMessage: "",
    }),
    actions: {
        async callAPIs() {
            try {
                // dates
                const datesResponse = await fetch(
                    "http://127.0.0.1:5000/dates"
                );
                this.dates = await datesResponse.json();

                // products
                const productsResponse = await fetch(
                    "http://127.0.0.1:5000/products"
                );
                this.products = await productsResponse.json();

                // stores
                const storesResponse = await fetch(
                    "http://127.0.0.1:5000/stores"
                );
                this.stores = await storesResponse.json();

                // transactions
                const transactionsResponse = await fetch(
                    "http://127.0.0.1:5000/transactions"
                );
                this.transactions = await transactionsResponse.json();
            } catch (error) {
                console.error(error.message);
                this.apiErrorMessage = error.message;
            }
        },
        async getQuantityOfItemsSold(
            groupby = "",
            dateId = "",
            storeId = "",
            productId = ""
        ) {
            try {
                const qtySoldsResponse = await fetch(
                    `http://127.0.0.1:5000/qty_items_sold?group_by=${groupby}&date_id=${dateId}&store_id=${storeId}&product_id=${productId}`
                );
                this.qty_solds = await qtySoldsResponse.json();
            } catch (error) {
                console.error(error.message);
                this.apiErrorMessage = error.message;
            }
        },
        async getGrossProfits(
            groupby = "",
            dateId = "",
            startDateId = "",
            endDateId = ""
        ) {
            try {
                const grossProfitsResponse = await fetch(
                    `http://127.0.0.1:5000/gross_profit?group_by=${groupby}&date_id=${dateId}&start_date_id=${startDateId}&end_date_id=${endDateId}`
                );
                this.gross_profits = await grossProfitsResponse.json();
            } catch (error) {
                console.error(error.message);
                this.apiErrorMessage = error.message;
            }
        },
        async getGrossMargins(
            groupby = "",
            dateId = "",
            startDateId = "",
            endDateId = ""
        ) {
            try {
                const grossMarginsResponse = await fetch(
                    `http://127.0.0.1:5000/gross_margin?group_by=${groupby}&date_id=${dateId}&start_date_id=${startDateId}&end_date_id=${endDateId}`
                );
                this.gross_margins = await grossMarginsResponse.json();
            } catch (error) {
                console.error(error.message);
                this.apiErrorMessage = error.message;
            }
        },
        async getInitData() {
            await this.callAPIs();
            await this.getQuantityOfItemsSold(
                "store",
                this.dates[this.dateInitIndex].id
            );
            await this.getGrossProfits(
                "store",
                this.dates[this.dateInitIndex].id
            );
            await this.getGrossMargins(
                "store",
                this.dates[this.dateInitIndex].id
            );
        },
    },
});
