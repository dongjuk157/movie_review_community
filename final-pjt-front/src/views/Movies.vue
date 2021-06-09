<template>
  <div>
    <h1 class="header">Movie</h1>
    <b-container class="d-flex">
      <b-row cols="1" cols-sm="2" cols-md="3" cols-lg="4"
        align-v="center" align-h="center"
      >
        <Card
          v-b-modal
          b-col
          b-d-flex
          b-align-items-stretch
          v-for="movie in movies"
          :key="movie.id"
          :movie="movie"
        />
      </b-row>
    </b-container>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import Card from '@/components/Card.vue'

export default {
  beforeCreate(){
  document.body.className = 'mvbackground'
  },
  name: 'Movies',
  components:{
    Card,
  },
  computed:{
    ...mapState([
      'movies'
    ])
  }
}
</script>

<style>
body.mvbackground{
  background: radial-gradient(rgb(150, 150, 150),black);
}
</style>