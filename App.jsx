import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar'
import Home from './pages/Home'
import Recipe from './pages/Recipe'
import NotFound from './pages/NotFound'

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/recipe" element={<Recipe />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Router>
  )
}

export default App