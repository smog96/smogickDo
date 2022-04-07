export const API_URLS = {
  // TODOs
  todos: "api/v1/todos",
  todoComplete: (id: number) => `/api/v1/todos/${id}/complete`,
  todoUncomplete: (id: number) => `/api/v1/todos/${id}/uncomplete`,
};
