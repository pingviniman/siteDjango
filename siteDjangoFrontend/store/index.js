import Vuex from 'vuex'

const createStore = () => {
  return new Vuex.Store({
    state: {
      persons: []
    },
    mutations: {
      set (state, info) {
        state.persons = info
      }
    }
  })
}

export default createStore
