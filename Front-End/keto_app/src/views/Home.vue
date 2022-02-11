<template>
  <div class="home">
    <div v-if="this.$store.state.isAuthenticated" class="cont">
      <!-- <div v-if="week">{{week}}</div> -->
      <div class="flex-row">
        <div v-if="this.weekData">
          <BarChart :chartData="weekData" :chartOptions="weekOptions" />  
        </div>
        <DatePicker class="cal" mode="date" v-model="date" :attributes='attrs'/>
        <div class="day-card">
          <div class="day-head">{{header}}</div>
          <div v-if="this.day && this.$store.state.user.id" >
            <DayCard :date="this.day" />
          </div>
          <div v-if="this.$store.state.day">
            <MainDay />
          </div>
            <AddFood :date="this.day"/>
        </div>
      </div>
      <div v-if="this.$store.state.day" class="flex-row dough">
        <div class="nut">
          <DoughnutChart :chartData="sugarData" />
        </div>
        <div class="nut">
          <DoughnutChart class="nut" :chartData="carbData" />
        </div>
        <div class="nut">
          <DoughnutChart :chartData="fatData" />
        </div>
      </div>
    </div>
    <div v-else>
      Please Login
    </div>
  </div>
</template>

<script>
import { Calendar, DatePicker } from 'v-calendar';
import 'v-calendar/dist/style.css';
import DayCard from '../components/DayCard.vue'
import MainDay from '../components/MainDay.vue'
import AddFood from '../components/AddFood.vue'

import { DoughnutChart, BarChart } from 'vue-chart-3';
import axios from 'axios'
export default {
  name: 'Home',
  components: {
    Calendar,
    DatePicker,
    DayCard,
    MainDay,
    AddFood,
    DoughnutChart,
    BarChart
  },
  data() {
    return {
      date: new Date(),
      attrs: [
        {
          key: 'today',
          highlight: {
          color: 'blue',
          fillMode: 'outline',
        },
          dates: new Date(),
        },
      ],
      weekData: null
    }
  },
  watch: {
    date(){
      this.getAllDays()
    }
  },
   mounted(){
    this.getAllDays()
  },
  // updated(){
  //   this.getAllDays()
  // },
  computed: {
    carbData(){
      let color = '#3181CE'
      let rem_carbs = this.$store.state.profile.daily_carb-this.$store.state.curCarbs
      if (rem_carbs<= 0){
        rem_carbs = 0
        color = 'rgb(165, 70, 70)';
      }
      return {
        labels: ['Carbs', 'Remaining Carbs'],
        datasets: [
          {
            data: [this.$store.state.curCarbs.toFixed(1), (rem_carbs.toFixed(1))],
            backgroundColor: [color, 'white'],
          },
        ],
      }
    },
    sugarData(){
      let color = '#123E6B'
      let rem_carbs = this.$store.state.profile.daily_sugar-this.$store.state.curSugar
      if (rem_carbs<= 0){
        rem_carbs = 0
        color = 'rgb(165, 70, 70)';
      }
      return {
        labels: ['Sugars', 'Remaining Sugars'],
        datasets: [
          {
            data: [this.$store.state.curSugar.toFixed(1), (rem_carbs.toFixed(1))],
            backgroundColor: [color, 'white'],
          },
        ],
      }
    },
    fatData(){
      let color = '#77CEFF'
      let rem_carbs = this.$store.state.profile.daily_fat-this.$store.state.curFat
      if (rem_carbs<= 0){
        rem_carbs = 0
        color = '#8ee696';
      }
      return {
        labels: ['Fats', 'Needed Fats'],
        datasets: [
          {
            data: [this.$store.state.curFat.toFixed(1), (rem_carbs.toFixed(1))],
            backgroundColor: [color, 'white'],
          },
        ],
      }
    },
    weekOptions(){
      return {
        plugins: {
            title: {
                display: false,
                text: 'Custom Chart Title'
            }
        }
      }
    },
    day(){
      // console.log(this.date)
      let date =  this.date.toLocaleString('en-US').slice(0,9)
      // console.log(date)
      let newDate = date.replace(',', '')
      let splitArr = newDate.split("/")
      let month = ''
      let day = ''
      if (splitArr[0].length === 1){
        month = `0${splitArr[0]}`
      } else{
        month = `${splitArr[0]}`
      }
      if (splitArr[1].length === 1){
        day = `0${splitArr[1]}`
      } else {
        day = `${splitArr[1]}`
      }
      let finalDate = `${splitArr[2]}-${month}-${day}`
      // console.log(finalDate)
      return finalDate
    },
    header(){
      let options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }
      return this.date.toLocaleString('en-US', options)
    },
    // week(){
    //   let date = this.date
    //   let arr = [];
    //   date.setDate(date.getDate() - date.getDay());
    //   for (let i = 0; i < 7; i++) {
    //     let curDate = new Date(date.setDate(date.getDate()));
    //     arr.push(curDate);
    //     date.setDate(date.getDate() + 1);
    //   }
    //   function formatDate(dateFormat) {
    //     let date = dateFormat.toLocaleString('en-US').slice(0, 9);
    //     let newDate = date.replace(',', '');
    //     let splitArr = newDate.split('/');
    //     let month = '';
    //     let day = '';
    //     if (splitArr[0].length === 1) {
    //       month = `0${splitArr[0]}`;
    //     } else {
    //       month = `${splitArr[0]}`;
    //     }
    //     if (splitArr[1].length === 1) {
    //       day = `0${splitArr[1]}`;
    //     } else {
    //       day = `${splitArr[1]}`;
    //     }
    //     let finalDate = `${splitArr[2]}-${month}-${day}`;
    //     return finalDate;
    //   }
    //   const finalArr = arr.map((day) => formatDate(day));
    //   console.log(this.$store.state.allDays)
    //   let id = this.$store.state.user.id
    //   let newArr = []
    //   for (let i=0; i<finalArr.length; i++){
    //     const result = this.$store.state.allDays.filter(day => day.user_id===id && day.date===finalArr[i])
    //     console.log(result, result.length)
    //     if (result.length === 0){
    //       newArr.push(0)
    //     }else{
    //       let totalCarbs = result[0].food_list.reduce(function (accumulator, food) {
    //         return accumulator + food.carbs;
    //       }, 0);
    //       newArr.push(totalCarbs)
    //     }
    //   }
    //   return(newArr);
    // },
    // weekData(){
    //   console.log('hello')
    //   return {
    //     labels: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
    //     datasets: [
    //       {
    //         // data: [this.week[0].toFixed(1), this.week[1].toFixed(1), this.week[2].toFixed(1), this.week[3].toFixed(1), this.week[4].toFixed(1), this.week[5].toFixed(1), this.week[6].toFixed(1)],
    //         data: [34.2, 34.4, 56.5, 32.52313123, 45.5, 65.532434, 32.3535363],
    //         backgroundColor: ['#77CEFF', '#0079AF', '#123E6B', '#97B0C4', '#A5C8ED', '#77CEFF', '#0079AF'],
    //       },
    //     ],
    //   }
    // },
  },
  methods:{
    async getAllDays(){
      const res = await axios.get(`http://127.0.0.1:8000/days`)
      let allDays = res.data
      let date = this.date
      let arr = [];
      date.setDate(date.getDate() - date.getDay());
      for (let i = 0; i < 7; i++) {
        let curDate = new Date(date.setDate(date.getDate()));
        arr.push(curDate);
        date.setDate(date.getDate() + 1);
      }
      function formatDate(dateFormat) {
        let date = dateFormat.toLocaleString('en-US').slice(0, 9);
        let newDate = date.replace(',', '');
        let splitArr = newDate.split('/');
        let month = '';
        let day = '';
        if (splitArr[0].length === 1) {
          month = `0${splitArr[0]}`;
        } else {
          month = `${splitArr[0]}`;
        }
        if (splitArr[1].length === 1) {
          day = `0${splitArr[1]}`;
        } else {
          day = `${splitArr[1]}`;
        }
        let finalDate = `${splitArr[2]}-${month}-${day}`;
        return finalDate;
      }
      const finalArr = arr.map((day) => formatDate(day));
      let id = this.$store.state.user.id
      let newArr = []
      for (let i=0; i<finalArr.length; i++){
        const result = allDays.filter(day => day.user_id===id && day.date===finalArr[i])
        console.log(result, result.length)
        if (result.length === 0){
          newArr.push(0)
        }else{
          let totalCarbs = result[0].food_list.reduce(function (accumulator, food) {
            return accumulator + food.carbs;
          }, 0);
          newArr.push(totalCarbs)
        }
      }
      console.log('NEWARR:', newArr)
      this.weekData = {
        labels: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
        datasets: [
          {
            data: [newArr[0].toFixed(1), newArr[1].toFixed(1), newArr[2].toFixed(1), newArr[3].toFixed(1), newArr[4].toFixed(1), newArr[5].toFixed(1), newArr[6].toFixed(1)],
            // data: [34.2, 34.4, 56.5, 32.52313123, 45.5, 65.532434, 32.3535363],
            backgroundColor: ['#77CEFF', '#0079AF', '#123E6B', '#97B0C4', '#A5C8ED', '#77CEFF', '#0079AF'],
          },
        ],
      }
    }
  }
}
</script>

<style scoped>
.cont{
  display: flex;
  flex-direction: column;
}
.flex-row {
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex: wrap;
}
.dough{
  display: flex;
  margin-top: 20px;
  align-items: center;
}
.day-head{
  font-weight: 600
}
.day-card{
  padding: 10px;
  background-color: white;
  border-radius: 8px;
  border: 1px solid rgb(214, 214, 214);
  box-shadow: 0px 0px 12px -5px rgba(0,0,0,0.7)
}
.cal{
  box-shadow: 0px 0px 12px -5px rgba(0,0,0,0.7)
}
</style>