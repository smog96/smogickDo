import { AxiosResponse } from "axios";
import { API_URLS } from "../constants";
import { http } from "./http";
import { TodoTask } from "../models/ApiModels";

export class ApiService {
  // TodoS
  static fetchTodos = (params: { skip: number; limit: number }) => {
    return http.get(API_URLS.todos);
  };
}
