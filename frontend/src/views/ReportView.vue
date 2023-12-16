<template>
  <v-container>
    <v-row>
      <!-- F1 -->
      <v-col cols="4">
        <!-- <v-card title="Fact 1" subtitle="Quantity (Grain) " class="elevation-4">
          <canvas id="ChartF1"></canvas>
        </v-card> -->
        <MyCard title="Fact 1" subtitle="Quantity (Grain)" />
      </v-col>

      <!-- F2 -->
      <v-col cols="4">
        <v-card
          title="Fact 2"
          subtitle="Fact 1 per Dimension 1, 2"
          class="elevation-4"
        >
          <canvas id="ChartF2"></canvas>
        </v-card>
      </v-col>

      <!-- F4 -->
      <v-col cols="4">
        <v-card
          title="Fact 4"
          subtitle="Derived Fact per Dimension 1, 2 (Extended Sales Dollar Amount
              (Omset))"
          class="elevation-4"
        >
          <v-card-subtitle>
            <v-row>
              <v-col cols="4"><MyDateSelector /></v-col>
            </v-row>
          </v-card-subtitle>
          <!-- <canvas id="ChartF2"></canvas> -->
        </v-card>
      </v-col>

      <!-- F11 -->
      <v-col cols="3">
        <v-card
          title="Fact 11"
          subtitle="Date Dimension Table"
          class="elevation-4"
        >
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
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import MyCard from "../components/MyCard.vue";
import MyDateSelector from "../components/MyDateSelector.vue";
import { useFetchedStore } from "../stores/Fetched";

export default {
  setup() {
    const myStore = useFetchedStore();
    return { myStore };
  },
  components: { MyCard, MyDateSelector },
  data() {
    return {
      dates: [],
      products: [],
      stores: [],
      transactions: [],

      // component variables
      f4_selected_date: "Select Date",
    };
  },
  // mounted() {
  //   // MOUNTED CHARTS
  //   // options
  //   const chartOptions = {
  //     // scales: {
  //     //   y: {
  //     //     beginAtZero: true,
  //     //   },
  //     // },
  //     animations: {
  //       tension: {
  //         duration: 1000,
  //         easing: "linear",
  //         from: 1,
  //         to: 0,
  //         loop: true,
  //       },
  //     },
  //   };

  //   // F1
  //   const f1c = document.getElementById("ChartF1");
  //   new Chart(f1c, {
  //     type: "bar",
  //     data: {
  //       labels: [
  //         "Bengbeng",
  //         "Potabe",
  //         "Milku",
  //         "Mie Goreng",
  //         "Sikat Gigi",
  //         "Beras 10kg",
  //       ],
  //       datasets: [
  //         {
  //           label: "# of Quantities",
  //           data: [12, 19, 3, 5, 2, 3],
  //           borderWidth: 1,
  //         },
  //       ],
  //     },
  //     options: chartOptions,
  //   });

  //   // F2
  //   const f2c = document.getElementById("ChartF2");
  //   new Chart(f2c, {
  //     type: "line",
  //     data: {
  //       labels: [1, 2, 3, 4, 5, 6, 7],
  //       datasets: [
  //         {
  //           label: "My First Dataset",
  //           data: [65, 59, 80, 81, 56, 55, 40],
  //           fill: false,
  //           borderColor: "rgb(75, 192, 192)",
  //           tension: 0.1,
  //         },
  //       ],
  //     },
  //     options: chartOptions,
  //   });
  // },
};
</script>
<style></style>
