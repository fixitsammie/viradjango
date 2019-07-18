import messageService from '../../services/messageService'

const state = {
  messages: [],
  bitcoin:[]
}

const getters = {
  bitcoin: state => {
    return state.bitcoin
  },
  messages: state => {
    return state.messages
  }
   

}

const actions = {
  getMessages ({ commit }) {
    messageService.fetchMessages()
    .then(messages => {
      commit('setMessages', messages)
    })
  },
  getbitcoin ({ commit }) {
    
    messageService.getBTC()
    .then(bitcoin => {
      commit('setBitcoin', bitcoin)
    })
  },
  addMessage({ commit }, message) {
    messageService.postMessage(message)
    .then(() => {
      commit('addMessage', message)
    })
  },
  deleteMessage( { commit }, msgId) {
    messageService.deleteMessage(msgId)
    commit('deleteMessage', msgId)
  }
}

const mutations = {
  setMessages (state, messages) {
    state.messages = messages
  },
  setBitcoin (state, bitcoin) {
    state.bitcoin = bitcoin
  },
  addMessage(state, message) {
    state.messages.push(message)
  },
  deleteMessage(state, msgId) {
    state.messages = state.messages.filter(obj => obj.pk !== msgId)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}