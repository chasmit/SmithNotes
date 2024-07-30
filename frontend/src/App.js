import React from 'react';
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';

import Header from "./components/Header";
import NoteForm from './components/NoteForm';
import NoteGrid from "./components/NoteGrid";
import Sidebar from './components/Sidebar';

import './App.css';

function App() {
  return (
    <Router>
      <div className="app-container">
        <Header />
        <div className="app">
          <Sidebar className="app-sideview"/>
          <Routes>
            <Route path="/" element={<NoteGrid/>} exact/>
            <Route path="/form" element={<NoteForm/>} exact/>
            <Route path="/form/:id" element={<NoteForm/>} exact/> 
          </Routes>
        </div>
      </div>
    </Router>
  )
}

export default App;
