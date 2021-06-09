import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins:[
    createPersistedState(),
  ],
  state: {
    windowWidth: 0,
    userId: null,
    userName: null,
    isLogin: false,
    movies: [],
    selectMovie: {},
    reviews: [],
    selectReview: {},
    myPageMovies: [],
    top10list: [],
    topRateList: [],
    personalList: [],
    genres: {
      28: "액션",
      12: "모험",
      16: "애니메이션",
      35: "코미디",
      80: "범죄",
      99: "다큐멘터리",
      18: "드라마",
      10751: "가족",
      14: "판타지",
      36: "역사",
      27: "공포",
      10402: "음악",
      9648: "미스터리",
      10749: "로맨스",
      878: "SF",
      10770: "TV 영화",
      53: "스릴러",
      10752: "전쟁",
      37: "서부",
    },
  },
  mutations: {
    isLogin(state, token){  
      state.isLogin = true
      state.userId = token.user_id
      state.userName = token.username
    },
    loadData(state, data){
      state.movies.push(...data)
    },
    selectMovie(state, movie){
      state.selectMovie = movie
    },
    logout(state){
      state.isLogin = false
      state.userId = null
      state.userName = null
    },
    getReviews(state, reviews){
      state.reviews = reviews
    },
    getMyPageMovies(state, movies){
      state.myPageMovies = movies
    },
    getTop10Movies(state, movies){
      state.top10list = movies
    },
    getTopRateMovies(state, movies){
      state.topRateList = movies
    },
    getPersonalMovies(state, movies){
      state.personalList = movies
    },
    updateWindowWidth(state, size){
      state.windowWidth = size
    }
  },
  actions: {
    isLogin(context){
      const JWT = localStorage.getItem('jwt')
      if (JWT){
        const decode = function parseJwt (token) {
          var base64Url = token.split('.')[1];
          var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
          var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
              return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
          }).join(''));
          return JSON.parse(jsonPayload);
        };
        return context.commit('isLogin', decode(JWT))
      }
    },
    loadData(context, data){
      return context.commit('loadData', data)
    },
    selectMovie(context, movie){
      return context.commit('selectMovie', movie)
    },
    logout(context){
      return context.commit('logout')
    },
    getReviews(context, reviews){
      const newReviews = reviews.map((review)=>{
        review.movie -= 1
        return review
      })
      return context.commit('getReviews', newReviews)
    },
    getMyPageMovies(context, movies){
      return context.commit('getMyPageMovies', movies)
    },
    getTop10Movies(context, movies){
      return context.commit('getTop10Movies', movies)
    },
    getTopRateMovies(context, movies){
      return context.commit('getTopRateMovies', movies)
    },
    getPersonalMovies(context, movies){
      return context.commit('getPersonalMovies', movies)
    },
    updateWindowWidth(context, size){
      return context.commit('updateWindowWidth', size)
    }

  },
  getters:{
    loginCheck(state){
      return state.isLogin
    },
    getUser(state){
      return {
        userId: state.userId,
        userName: state.userName,
      }
    },
    getMovies(state){
      return state.movies
    },
    getSelectMovie(state){
      return state.selectMovie
    },
    getReviews(state){
      return state.reviews
    },
    getSelectReview(state){
      return state.selectReview
    },
    getMyPageMovies(state){
      return state.myPageMovies
    },
    getTop10list(state){
      return state.top10list
    },
    getTopRateList(state){
      return state.topRateList
    },
    getPersonalList(state){
      return state.personalList
    },
  },
  modules: {
  },
})
