<template>
  <b-modal size="xl"
    :id="'myModal'+modalName+movieId" :title="movieTitle" 
    @show="onClick"
    hide-header-close
  >
    <div>
      <div class="d-flex flex-wrap justify-content-stretch">
        <!-- 영화 포스터 -->
        <b-col class="p-3 col-12 col-lg-4">
          <img style="width:100%"
            :src="moviePoster" :alt="movieTitle+'poster'"
          >
        </b-col>
        <b-col class="p-3 col-12 col-lg-8">
          <div class="wrapper">
            <!-- 영화 관련 -->
            <iframe class="player"
              id="ytplayer" type="text/html" 
              :src="this.url"
              frameborder="0">
            </iframe>
          </div>
          <div>
            <h3>
              {{movieTitle}}
              <b-button class="bg-light" @click="likeToggle" v-if="isNotTopRate">
                <span v-if="like">
                  <font-awesome-icon :icon="['fas','heart']" :style="{color : 'red'}" />
                </span>
                <span v-else>
                  <font-awesome-icon :icon="['far','heart']" :style="{color : 'black'}"/>
                </span>
              </b-button>
            </h3>
          </div>

          <div>
            <p><strong>줄거리</strong></p>
            <p style="font-family: 'Nanum Gothic', sans-serif;">{{movieOverview}}</p>
          </div>
          <p><strong>개봉일:</strong> {{movieReleaseDate}}</p>
          <p><strong>평점:</strong> {{movieVoteAverage}}</p>
          <div v-if="isNotTopRate">
            <p><strong>리뷰:</strong></p>
            <p v-for="review in reviewList" :key="review.id" 
              style="font-family: 'Nanum Gothic', sans-serif;"> 
              - <a href="#" @click.prevent="moveReview(review)">
               {{review.title}}
              </a>

            </p>
            <button class="btn btn-outline-primary" @click="createReview">리뷰 작성</button>
          </div>
        </b-col>
      </div>
    </div>
  </b-modal>
</template>

<script>
import axios from 'axios'
const BASE_URL = "https://www.youtube.com/embed/"
export default {
  props:{
    movie:{
      type: Object,
    },
    modalName:{
      type: String,
    },
  },
  data(){
    return {
      url: '',
      reviewList: [],
      like: false,
    }
  },
  methods:{
    onClick(){
      const movie_id = this.movie.movie_id
      if(this.modalName !== 'topRate'){
        axios({
          method: 'get',
          url:`http://127.0.0.1:8000/movies/like/${movie_id}/`,
          headers: {
            Authorization: `JWT ${localStorage.getItem('jwt')}`, 
          },
        })
          .then((res)=>{
          if (res.data.like)
            this.like = true
        }).catch((e)=>{
          console.log(e)
        })
      }

      const API_KEY = ''
      const params = {
        method: 'get',
        url:`https://api.themoviedb.org/3/movie/${movie_id}/videos?api_key=${API_KEY}&language=ko-KR`
      }
      axios(params)
        .then((res)=>{
        const videoList = res.data.results
        if (videoList.length > 0){
          for (let video of videoList){
            if (video.type==="Trailer")
              this.url = BASE_URL + video.key +'?autoplay=1'
            break
          }
          if (this.url==='')
            this.url = BASE_URL + videoList[0].key +'?autoplay=1'
        }
        else{
          const YOUTUBE_API_KEY = ''
          const youtube_config = {
            method: 'get',
            url: 'https://www.googleapis.com/youtube/v3/search',
            params:{
              key: YOUTUBE_API_KEY,
              part: 'snippet',
              type: 'video',
              q: this.movieTitle,
              maxResults: 1,
            }
          }
          axios(youtube_config)
            .then((res)=>{
              this.url = BASE_URL + res.data.items[0].id.videoId +'?autoplay=1'
          }).catch(e=>{
            console.log(e)
          })
        }
      }).catch((e)=>{
        console.log(e)
      })
      const params2 = { 
        method: 'get',
        url:`http://127.0.0.1:8000/review/${movie_id}/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`, 
        },
      }
      if(this.modalName !== 'topRate'){
        axios(params2)
          .then((res)=>{
          this.reviewList = res.data
        }).catch((e)=>{
          console.log(e)
        })
      }
    },
    createReview(){
      this.$store.state.selectMovie = this.movie
      this.$router.push({name:'CreateReview'})
    },
    likeToggle(){
      const movie_id = this.movie.movie_id
      const params = {
        method: 'post',
        url:`http://127.0.0.1:8000/movies/like/${movie_id}/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`, 
        },
      }
      axios(params)
        .then((res)=>{
        if (res.data.like)
          this.like = true
        else
          this.like = false
      }).catch((e)=>{
        console.log(e)
      })
    },
    moveReview(review){
      this.$store.state.selectReview = review
      this.$router.push({name: 'ReviewDetail'})
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
    isNotTopRate(){
      if (this.modalName === 'topRate') 
        return false
      return true
    }
  },

  
}
</script>

<style>
@import url(//fonts.googleapis.com/earlyaccess/nanumgothic.css);
  .wrapper {
    position: relative;
    width: 100%;
    padding-bottom: 56.25%;
    margin-bottom: 1vw;
  }

  .player {
    position: absolute;
    width: 100%;
    height: 100%;
    background: #000;
  }
</style>
