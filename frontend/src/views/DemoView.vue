<template>
  <v-container>
    <v-row>
      <!-- Buy Product -->
      <v-col cols="6">
        <v-row class="elevation-4 rounded pa-3 ma-0">
          <v-col>
            <v-form>
              <!-- title -->
              <div class="text-h5">Buy Product</div>
              <div class="text-caption mb-5">
                Demo of buying a product (customer transaction)
              </div>

              <!-- multiselect -->
              <v-select
                clearable
                chips
                label="Product"
                v-model="selectedBuyProducts"
                :items="productsA"
                :item-props="itemProps"
                multiple
                variant="outlined"
              ></v-select>

              <!-- product details -->
              <v-row no-gutters class="mt-5">
                <template
                  v-for="(prd, index) in selectedBuyProducts"
                  :key="index"
                >
                  <v-col cols="8">
                    <div class="text-body-1">{{ prd.name }}</div>
                    <div class="text-caption">
                      {{ formatRupiah(prd.price) }}
                    </div>
                  </v-col>

                  <v-col cols="4" class="d-flex align-center justify-end">
                    <div
                      class="btn-group btn-group-sm"
                      role="group"
                      aria-label="Basic outlined example "
                      outline
                    >
                      <v-btn
                        type="button"
                        size="small"
                        class="btn"
                        @click="decrementQtyBP(prd)"
                        >-</v-btn
                      >
                      <span class="px-3 elevation-4">{{ prd.qty }}</span>
                      <v-btn
                        type="button"
                        size="small"
                        class="btn"
                        @click="incrementQty(prd)"
                        >+</v-btn
                      >
                    </div>
                  </v-col>
                  <v-divider></v-divider>
                </template>
              </v-row>

              <!-- summary -->
              <div class="text-button mt-5 text-end d-flex flex-column">
                <div class="text-caption">Total Price:</div>
                <span class="text-h6 mb-3">{{
                  formatRupiah(totalPriceBuyProduct)
                }}</span>
              </div>
              <v-btn block class="bg-success" prepend-icon="mdi-cash-fast"
                >Buy</v-btn
              >
            </v-form>
          </v-col>
        </v-row>
      </v-col>

      <!-- Add Product -->
      <v-col cols="6">
        <v-row class="elevation-4 rounded pa-3 ma-0">
          <v-col>
            <v-form>
              <!-- title -->
              <div class="text-h5">Add Product</div>
              <div class="text-caption mb-5">
                Demo of adding product to store inventory (stock transaction)
              </div>

              <!-- multiselect -->
              <v-select
                clearable
                chips
                label="Product"
                v-model="selectedAddProducts"
                :items="productsB"
                :item-props="itemProps"
                multiple
                variant="outlined"
              ></v-select>

              <!-- product details -->
              <v-row no-gutters class="mt-5">
                <template
                  v-for="(prd, index) in selectedAddProducts"
                  :key="index"
                >
                  <v-col cols="8">
                    <div class="text-body-1">{{ prd.name }}</div>
                    <div class="text-caption">
                      {{ formatRupiah(prd.price) }}
                    </div>
                  </v-col>

                  <v-col cols="4" class="d-flex align-center justify-end">
                    <div
                      class="btn-group btn-group-sm"
                      role="group"
                      aria-label="Basic outlined example "
                      outline
                    >
                      <v-btn
                        type="button"
                        size="small"
                        class="btn"
                        @click="decrementQtyAP(prd)"
                        >-</v-btn
                      >
                      <span class="px-3 elevation-4">{{ prd.qty }}</span>
                      <v-btn
                        type="button"
                        size="small"
                        class="btn"
                        @click="incrementQty(prd)"
                        >+</v-btn
                      >
                    </div>
                  </v-col>
                  <v-divider></v-divider>
                </template>
              </v-row>

              <!-- summary -->
              <div class="text-button mt-5 text-end d-flex flex-column">
                <div class="text-caption">Total Qty:</div>
                <span class="text-h6 mb-3">{{ totalQtyAddProduct }}</span>
              </div>
              <v-btn block class="bg-success" prepend-icon="mdi-truck-delivery"
                >Add</v-btn
              >
            </v-form>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
  <div v-for="(p, index) in products" :key="index">
    {{ p.name }}
    {{ p.qty }}
    {{ p.price }}
  </div>
  <p></p>
  <div v-for="(p, index) in selectedBuyProducts" :key="index">
    {{ p.name }}
    {{ p.qty }}
    {{ p.price }}
  </div>
  <p></p>
  <div v-for="(p, index) in selectedAddProducts" :key="index">
    {{ p.name }}
    {{ p.qty }}
    {{ p.price }}
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedBuyProducts: [],
      selectedAddProducts: [],
      productsA: [
        { name: "pA", qty: 1, price: 20000 },
        { name: "amnsngdagsjfhaskdhkjaskd", qty: 1, price: 1000 },
        { name: "pC", qty: 1, price: 30000 },
      ],
      productsB: [
        { name: "pA", qty: 1, price: 20000 },
        { name: "amnsngdagsjfhaskdhkjaskd", qty: 1, price: 1000 },
        { name: "pC", qty: 1, price: 30000 },
      ],
    };
  },
  methods: {
    itemProps(item) {
      return {
        title: item.name,
      };
    },
    formatRupiah(number) {
      const formatter = new Intl.NumberFormat("id-ID", {
        style: "currency",
        currency: "IDR",
        minimumFractionDigits: 2,
      });
      return formatter.format(number);
    },
    incrementQty(product) {
      product.qty++;
    },
    decrementQtyBP(product) {
      if (product.qty > 1) {
        product.qty--;
      } else {
        const index = this.selectedBuyProducts.indexOf(product);
        if (index !== -1) {
          this.selectedBuyProducts.splice(index, 1);
        }
      }
    },
    decrementQtyAP(product) {
      if (product.qty > 1) {
        product.qty--;
      } else {
        const index = this.selectedAddProducts.indexOf(product);
        if (index !== -1) {
          this.selectedAddProducts.splice(index, 1);
        }
      }
    },
  },
  computed: {
    totalPriceBuyProduct() {
      let total = 0;
      for (let i = 0; i < this.selectedBuyProducts.length; i++) {
        total +=
          this.selectedBuyProducts[i].price * this.selectedBuyProducts[i].qty;
      }
      return total;
    },
    totalQtyAddProduct() {
      let total = 0;
      for (let i = 0; i < this.selectedAddProducts.length; i++) {
        total += this.selectedAddProducts[i].qty;
      }
      return total;
    },
  },
};
</script>
<style></style>
