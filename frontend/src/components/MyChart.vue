<template>
  <slot> </slot>
  <canvas ref="theChart"></canvas>
</template>
<script>
import { limitWords } from "../utils/string_formatter";
import { shallowRef } from "vue";

export default {
  props: ["type", "labels", "label", "data", "x_unit", "y_unit"],
  data() {
    return {
      chartInstance: null,
    };
  },
  methods: {
    updateChart() {
      this.chartInstance.config.data.datasets[0].data = this.data;
      this.chartInstance.config.data.labels = this.labels;
      this.chartInstance.update();
    },
    renderChart() {
      const chartOptions = {
        scales: {
          x: {
            title: {
              display: true,
              text: this.x_unit, // X-axis title
              color: "black", // Adjust the title color
              font: {
                family: "var(--v-font-family)",
              },
            },
          },
          y: {
            title: {
              display: true,
              text: this.y_unit, // Y-axis title
              color: "black", // Adjust the title color
              font: {
                family: "var(--v-font-family)",
              },
            },
          },
        },
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

      // Create a new chart instance
      this.chartInstance = shallowRef(
        new Chart(this.$refs.theChart, {
          type: this.type,
          data: {
            labels: this.labels.map((e) => (e ? limitWords(e, 18) : "")),
            datasets: [
              {
                label: this.label,
                data: this.data,
              },
            ],
          },
          options: ["pie", "doughnut", "polarArea"].includes(this.type)
            ? null
            : this.chartOptions,
        })
      );
    },
  },
  mounted() {
    this.renderChart();
  },
};
</script>
