import * as types from "../types";
export default {
  [types.Menu_SELECT](state, name) {
    state.activeName = name;
  },
  [types.FOLLOW_SELECT](state, type) {
    state.fanType = type;
  },
};
