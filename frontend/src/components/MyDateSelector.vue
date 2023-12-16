<template>
  <v-menu location="bottom">
    <template v-slot:activator="{ props }">
      <v-btn v-bind="props" size="small" color="primary elevation-7">
        {{ f4_selected_date }}
      </v-btn>
    </template>
    <v-list>
      <v-list-item
        v-for="(item, index) in items"
        :key="index"
        :value="f4_selected_date"
        @click=""
      >
        <v-list-item-title>{{ item.title }}</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-menu>
</template>
<script>
export default {};
</script>
