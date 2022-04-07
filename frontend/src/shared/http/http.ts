import axios, { AxiosInstance } from "axios";

export const BASE_URL = "";

export let http: AxiosInstance = axios.create({
  baseURL: BASE_URL,
});

export const initApi = (token?: string) => {
  try {
    // no auth on start
    //if (!!token) {
    // const headers = { Authorization: token };
    //http = axios.create({ headers, baseURL: BASE_URL });
    //return;
    // }

    http = axios.create({ baseURL: BASE_URL });
    return;
  } catch (error) {
    http = axios.create({ baseURL: BASE_URL });
  }
};
