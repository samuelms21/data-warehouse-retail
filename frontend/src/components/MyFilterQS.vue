<template>
  <v-card-subtitle>
    <v-row justify="start">
      <!-- groupby -->
      <MySelector
        :items="[{ name: 'store' }, { name: 'product' }]"
        :isDate="false"
        :useEmpty="false"
        :initIndex="0"
        @selectedItem="selectGroup"
      />
      <!-- dates -->
      <MySelector
        :items="myStore.dates"
        :isDate="true"
        :useEmpty="false"
        :initIndex="myStore.dateInitIndex"
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
      selectedGroup: null,
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
    async callRequest() {
      if (this.selectedDate) {
        await this.myStore.getQuantityOfItemsSold(
          this.selectedGroup.name,
          this.selectedDate.id,
          this.selectedStore ? this.selectedStore.id : "",
          this.selectedProduct ? this.selectedProduct.id : ""
        );
        this.$emit("emitChart");
        console.log(this.myStore.qty_solds);
      }
    },
    selectGroup(group) {
      this.selectedGroup = group;
      this.callRequest();
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
    this.selectedDate = this.myStore.dates[this.myStore.dateInitIndex];
    this.selectedGroup = { name: "store" };
  },
};
</script>
