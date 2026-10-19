
import { Routes, Route } from "react-router-dom";
import Article from "./Article";
import Header from "./Header";
import Home from "./Home";

function App() {
  return (
    <div className="App">
      <Header />

      <Routes>
        <Route
          path="/articles/:id"
          element={<Article />}
        />
        <Route
          path="/"
          element={<Home />}
        />
      </Routes>
    </div>
  );
}

export default App;
