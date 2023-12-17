<template>
  <v-card-subtitle>
    <v-row justify="start">
      <!-- dates -->
      <MySelector
        :items="myStore.dates"
        :isDate="true"
        :useEmpty="false"
        @selectedItem="selectDate"
      />
      <!-- stores -->
      <MySelector
        :items="myStore.stores"
        :isDate="false"
        :useEmpty="true"
        @selectedItem="selectStore"
      />
      <!-- products -->
      <MySelector
        :items="myStore.products"
        :isDate="false"
        :useEmpty="true"
        @selectedItem="selectProduct"
      />
    </v-row>
  </v-card-subtitle>
</template>
<script>
import MySelector from "../components/MySelector.vue";
import { formatDate } from "../utils/string_formatter";
import { useFetchedStore } from "../stores/fetched";

export default {
  setup() {
    const myStore = useFetchedStore();
    return { myStore };
  },
  components: { MySelector },
  props: ["items", "null_statement", "isDate"],
  data() {
    return {
      selectedDate: null,
      selectedStore: null,
      selectedProduct: null,
    };
  },
  computed: {
    dateDisplayed() {
      if (this.selectedDate) {
        return this.listedDate(this.selectedDate.full_date);
      }
      return this.selectedDate;
    },
  },
  methods: {
    callRequest() {
      if (this.selectedDate.id) {
        this.myStore.getQuantityOfItemsSold(
          this.selectedDate.id,
          this.selectedStore ? this.selectedStore.id : null,
          this.selectedProduct ? this.selectedProduct.id : null
        );
        this.$emit("emitChart");
      }
    },
    selectDate(date) {
      this.selectedDate = date;
      this.callRequest();
    },
    selectStore(store) {
      this.selectedStore = store;
      this.callRequest();
    },
    selectProduct(product) {
      this.selectedProduct = product;
      this.callRequest();
    },
    listedDate(date) {
      return formatDate(date);
    },
  },
  mounted() {
    this.selectedDate = this.myStore.dates[0];
    // this.callRequest();
    console.log(this.myStore.qty_solds);
  },
};
</script>
