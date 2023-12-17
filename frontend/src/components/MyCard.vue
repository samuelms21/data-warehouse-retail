<template>
  <v-col :cols="cols">
    <v-card :title="title" :subtitle="subtitle" class="elevation-4">
      <slot> </slot>
    </v-card>
  </v-col>
</template>
<script>
export default {
  props: ["cols", "title", "subtitle"],
};
</script>
