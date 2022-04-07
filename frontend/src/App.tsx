import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import "./App.css";
import { TodoPage } from "./components/todo/TodoPage";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/todo" element={<TodoPage />}></Route>
          <Route path="" element={<Navigate to="/todo" />}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
