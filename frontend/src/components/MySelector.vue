<template>
  <v-col cols="3">
    <v-menu location="bottom">
      <template v-slot:activator="{ props }">
        <v-btn
          v-bind="props"
          size="small"
          color="primary elevation-7"
          width="200"
        >
          {{ buttonName }}
        </v-btn>
      </template>
      <v-list>
        <v-list-item v-if="useEmpty" @click="selectItem(null)">
          <v-list-item-title> None </v-list-item-title>
        </v-list-item>
        <v-list-item
          v-for="(item, index) in items"
          :key="index"
          @click="selectItem(item)"
        >
          <v-list-item-title>{{
            isDate ? listedDate(item.full_date) : item.name
          }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </v-col>
</template>
<script>
import { formatDate, limitWords } from "../utils/string_formatter";

export default {
  props: ["items", "isDate", "useEmpty"],
  data() {
    return {
      selectedItem: null,
    };
  },
  computed: {
    buttonName() {
      if (this.selectedItem) {
        if (this.isDate) {
          return limitWords(this.listedDate(this.selectedItem.full_date), 14);
        } else {
          return limitWords(this.selectedItem.name, 14);
        }
      }
      return "None";
    },
  },
  methods: {
    selectItem(item) {
      this.selectedItem = item;
      this.$emit("selectedItem", this.selectedItem);
    },
    listedDate(date) {
      return formatDate(date);
    },
  },
  mounted() {
    if (!this.useEmpty) {
      this.selectedItem = this.items[0];
    }
  },
};
</script>
