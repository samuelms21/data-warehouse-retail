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
        />
      </MyCard>

      <!-- F2 -->
      <MyCard
        cols="4"
        title="Fact 2"
        subtitle="Fact 1 per Dimension 1, 2 (Total Sales)"
      >
        <MyChart
          type="bar"
          :labels="
            myStore.qty_solds.map(
              (e) => e.name ?? e.store_name ?? e.product_name
            )
          "
          label="# of Sold Products"
          :data="myStore.qty_solds.map((e) => e.total_sales_qty)"
          :useFilter="true"
          ref="chart-f2"
        >
          <MyFilterQS @emitChart="updateChart('f2')" />
        </MyChart>
      </MyCard>

      <!-- F4 -->
      <MyCard
        cols="4"
        title="Fact 4"
        subtitle="Derived Fact per Dimension 1, 2"
      >
        <div class="text-center">under development...</div>
      </MyCard>

      <!-- F7 -->
      <MyCard
        cols="4"
        title="Fact 7"
        subtitle="Additive Fact per Dimension 1, 2, 3 (Gross Profit)"
      >
        <MyChart
          type="bar"
          :labels="
            myStore.gross_profits.map(
              (e) => e.name ?? e.store_name ?? e.product_name
            )
          "
          label="# of Gross Profits"
          :data="myStore.gross_profits.map((e) => e.total_gross_profit)"
          :useFilter="true"
          ref="chart-f7"
          y_unit="$ (Dollar)"
        >
          <MyFilterES @emitChart="updateChart('f7')" api="gp" />
        </MyChart>
      </MyCard>

      <!-- F8 -->
      <MyCard
        cols="4"
        title="Fact 8"
        subtitle="Non-Additive Fact per Dimension 1, 2 (Gross Margin (%))"
      >
        <MyChart
          type="polarArea"
          :labels="
            myStore.gross_margins.map(
              (e) => e.name ?? e.store_name ?? e.product_name
            )
          "
          label="# of Gross Profits"
          :data="myStore.gross_margins.map((e) => e.gross_margin_percentage)"
          :useFilter="true"
          ref="chart-f8"
          y_unit="% (Percentage)"
        >
          <MyFilterES @emitChart="updateChart('f8')" api="gm" />
        </MyChart>
      </MyCard>

      <!-- F10 -->
      <MyCard
        cols="4"
        title="Fact 10"
        subtitle="Factless Fact per Dimension 1, 2 (Non-Promotion)"
      >
        <MyChart
          type="bar"
          :labels="
            myStore.gross_margins.map(
              (e) => e.name ?? e.store_name ?? e.product_name
            )
          "
          label="# of Gross Profits"
          :data="myStore.gross_margins.map((e) => e.gross_margin_percentage)"
          :useFilter="true"
          ref="chart-f10"
          y_unit="% (Percentage)"
        >
          <MyFilterES @emitChart="updateChart('f10')" api="gm" />
        </MyChart>
      </MyCard>

      <!-- F11 -->
      <MyCard cols="4" title="Fact 11" subtitle="Date Dimension Table">
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
  <v-btn @click="test">open console</v-btn>
</template>
<script>
import { useFetchedStore } from "../stores/fetched";
import MyFilterQS from "../components/MyFilterQS.vue";
import MyFilterES from "../components/MyFilterES.vue";
import MyChart from "../components/MyChart.vue";
import MyCard from "../components/MyCard.vue";

export default {
  setup() {
    const myStore = useFetchedStore();
    return { myStore };
  },
  components: { MyCard, MyChart, MyFilterQS, MyFilterES },
  data() {
    return {
      f1Data: Array(8)
        .fill()
        .map(() => Math.random() * 10),
      borderWidth: 1,
    };
  },
  methods: {
    updateChart(chartId) {
      this.$refs["chart-" + chartId].updateChart();
    },
    test() {
      const kk = [{}];
      console.log(kk.map((e) => e.name ?? e.store_name ?? e.product_name));
    },
  },
};
</script>
<style></style>
