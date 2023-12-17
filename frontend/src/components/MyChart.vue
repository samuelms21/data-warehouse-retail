<template>
  <MyFilter v-if="useFilter" @emitChart="updateChart" />
  <canvas ref="theChart"></canvas>
</template>
<script>
import MySelector from "../components/MySelector.vue";
import MyFilter from "../components/MyFilter.vue";
import { limitWords } from "../utils/string_formatter";

export default {
  props: ["type", "labels", "label", "data", "useFilter"],
  data() {
    return {
      chartInstance: null,
    };
  },
  components: { MyFilter, MySelector },
  methods: {
    renderChart() {
      const chartOptions = {
        // scales: {
        //   y: {
        //     beginAtZero: true,
        //   },
        // },
        animations: {
          tension: {
            duration: 1000,
            easing: "linear",
            from: 1,
            to: 0,
            loop: true,
          },
        },
      };

      // Destroy existing chart instance if it exists
      console.log(`HOOOOOOOOOOOOOOOOOOOOOO: ${this.label}`);
      if (this.chartInstance) {
        console.log(`this.chartInstance: ${this.chartInstance}`);
        this.chartInstance.destroy();
        // this.chartInstance = null;
      }

      // Create a new chart instance
      this.chartInstance = new Chart(this.$refs.theChart, {
        type: this.type,
        data: {
          labels: this.labels.map((e) => limitWords(e, 18)),
          datasets: [
            {
              label: this.label,
              data: this.data,
              // data: Array(this.labels.length)
              //   .fill()
              //   .map(() => Math.random() * 10),
              // borderWidth: 1,
            },
          ],
        },
        options: chartOptions,
      });
    },
    updateChart() {
      this.renderChart();
    },
  },
  mounted() {
    this.renderChart();
  },
};
</script>
