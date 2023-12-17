<template>
  <v-container>
    <v-row>
      <!-- F1 -->
      <MyCard cols="4" title="Fact 1" subtitle="Quantity (Grain)">
        <MyChart
          type="bar"
          :labels="myStore.products.map((e) => e.name)"
          label="# of Quantities"
          :data="f1Data"
          :useFilter="false"
        />
      </MyCard>

      <!-- F2 -->
      <MyCard cols="4" title="Fact 2" subtitle="Fact 1 per Dimension 1, 2">
        <div class="text-center">under development...</div>
      </MyCard>

      <!-- F4 -->
      <MyCard
        cols="4"
        title="Fact 4"
        subtitle="Derived Fact per Dimension 1, 2 (Quantity of Sold Items)"
      >
        <MyChart
          type="bar"
          :labels="myStore.qty_solds.map((e) => e.store_name)"
          label="# of Sold Products"
          :data="myStore.qty_solds.map((e) => e.total_sales_qty)"
          :useFilter="true"
        />
      </MyCard>

      <!-- F7 -->
      <!-- <MyCard
        cols="4"
        title="Fact 7"
        subtitle="Additive Fact per Dimension 1, 2, 3 (Total Sales)"
      >
        <MyChart
          type="bar"
          :labels="myStore.qty_solds.map((e) => e.store_name)"
          label="# of Sold Products"
          :data="myStore.qty_solds.map((e) => e.total_sales_qty)"
          :useFilter="true"
        />
      </MyCard> -->

      <!-- F11 -->
      <MyCard cols="3" title="Fact 11" subtitle="Date Dimension Table">
        <v-table fixed-header height="300px">
          <thead>
            <tr>
              <th class="text-left">Date</th>
              <th class="text-left">Dayname</th>
              <th class="text-left">Event</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in myStore.dates" :key="item.id">
              <td>
                {{ item.year_of_date }}-{{ item.month_of_year }}-{{
                  item.day_of_month
                }}
              </td>
              <td>{{ item.day_name }}</td>
              <td>{{ item.event_name ? item.event_name : "No Event" }}</td>
            </tr>
          </tbody>
        </v-table>
      </MyCard>
    </v-row>
  </v-container>
</template>
<script>
import MyCard from "../components/MyCard.vue";
import MyChart from "../components/MyChart.vue";
import { useFetchedStore } from "../stores/fetched";

export default {
  setup() {
    const myStore = useFetchedStore();
    return { myStore };
  },
  components: { MyCard, MyChart },
  data() {
    return {
      f1Data: Array(8)
        .fill()
        .map(() => Math.random() * 10),
      borderWidth: 1,
    };
  },
};
</script>
<style></style>
