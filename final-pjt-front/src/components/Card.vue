<template>
  <b-card-group>
    <b-card
      v-b-modal="'myModal'+ modalName + movieId"
      :img-src="moviePoster"
      :img-alt="movieTitle+'Poster'"
      img-height="100%"
      tag="article"
      style="max-width: 20rem;"
      align="center"
      no-body
      bg-variant="transparent"
      class="my-2 mx-auto"
    >
    <div class="description">
        <h4>
          {{movieTitle}}
        </h4>
        <div>
          {{movieGenres}}
        </div>
      </div>
    </b-card>
    <Modal 
      :movie="movie"
      :modalName="modalName"
    />
  </b-card-group>
</template>

<script>
import Modal from './Modal.vue'
export default {
  name:'Card',
  components: { 
    Modal,
  },
  props:{
    modalName:{
      type: String,
    },
    movie:{
      type: Object,
    }
  },
  computed:{
    movieTitle(){
      return this.movie.title
    },
    movieId(){
      return this.movie.movie_id
    },
    moviePoster(){
      return "https://image.tmdb.org/t/p/w500/" + this.movie.poster_path
    },
    movieOverview(){
      return this.movie.overview
    },
    movieReleaseDate(){
      return this.movie.release_date
    },
    movieVoteAverage(){
      return this.movie.vote_average
    },
    movieGenres(){
      const genre_text_list = []
      this.movie.genre_ids.split(',').forEach((genre)=>{
        if (genre)
          genre_text_list.push(this.$store.state.genres[Number(genre)])
      })
      return genre_text_list.join(', ')
    },
  },
}
</script>

<style>

</style>