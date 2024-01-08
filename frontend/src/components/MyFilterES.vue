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
                :useEmpty="true"
                :initIndex="myStore.dateInitIndex"
                @selectedItem="selectDate"
            />
            <!-- start date -->
            <MySelector
                :items="myStore.dates"
                :isDate="true"
                :useEmpty="true"
                @selectedItem="selectStartDate"
            />
            <!-- end date -->
            <MySelector
                :items="myStore.dates"
                :isDate="true"
                :useEmpty="true"
                @selectedItem="selectEndDate"
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
    props: ["items", "null_statement", "isDate", "api"],
    data() {
        return {
            selectedGroup: null,
            selectedDate: null,
            selectedStartDate: null,
            selectedEndDate: null,
            methodDict: {
                gp: this.crGrossProfits,
                gm: this.crGrossMargins,
            },
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
        async crGrossProfits() {
            if (this.selectedDate) {
                await this.myStore.getGrossProfits(
                    this.selectedGroup.name,
                    this.selectedDate.id,
                    this.selectedStartDate ? this.selectedStartDate.id : null,
                    this.selectedEndDate ? this.selectedEndDate.id : null
                );
                this.$emit("emitChart");
            }
        },
        async crGrossMargins() {
            if (this.selectedDate) {
                await this.myStore.getGrossMargins(
                    this.selectedGroup.name,
                    this.selectedDate.id,
                    this.selectedStartDate ? this.selectedStartDate.id : null,
                    this.selectedEndDate ? this.selectedEndDate.id : null
                );
                this.$emit("emitChart");
            }
        },
        selectGroup(group) {
            this.selectedGroup = group;
            this.methodDict[this.api]();
        },
        selectDate(date) {
            this.selectedDate = date;
            this.methodDict[this.api]();
        },
        selectStartDate(start) {
            this.selectedStartDate = start;
            this.methodDict[this.api]();
        },
        selectEndDate(end) {
            this.selectedEndDate = end;
            this.methodDict[this.api]();
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
