import * as types from "../types";
export default {
  [types.Menu_SELECT](state, name) {
    state.activeName = name;
  }
};
