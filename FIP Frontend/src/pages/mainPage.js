import React from 'react';
import { BrowserRouter as Router, Switch , Route, useRouteMatch } from 'react-router-dom';
import { Header } from '../components/Header'
import { AlumniHomePage } from './alumniHomePage';
import { StudentHomePage } from './studentHomePage';

export const HomePage = () => {
  const { path } = useRouteMatch()
  return (
    <Router>
      <Header />
      <AlumniHomePage />
      {/* <StudentHomePage /> */}
    </Router>
    );
  }

