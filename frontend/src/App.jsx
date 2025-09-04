import { useState } from 'react'
import './App.css'
import LocationCard from './components/Card'
import MainNavBar from './components/NavBar'

function App() {

  return (
    <>
      <MainNavBar></MainNavBar>
      <LocationCard
        locationName="Casa"
        locationImage="https://i.pinimg.com/1200x/24/2d/e0/242de0a8581dd00744edbe5d9b118a9d.jpg"
        xCoord="0"
        yCoord="0"
        zCoord="0"
        dimension="Overworld"
        notes="Test"
      ></LocationCard>
    </>
  )
}

export default App
