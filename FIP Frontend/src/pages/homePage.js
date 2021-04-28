import React from 'react';
import { BrowserRouter as Router, Switch , Route, Link } from 'react-router-dom';
import { AlumniSidebar } from '../sidebars/alumniSidebar';
import { Header } from '../components/Header'
import { DashboardPage } from './alumni/dashboardPage';
import AvailablePostsPage from './alumni/availablePosts';
import ResultsPage from './alumni/resultsPage';
import ProfilePage from './alumni/profilePage';
import CvPage from './alumni/cvPage';
import ProjectsPage from './alumni/projectsPage';
import ChatPage from './alumni/chatPage';
import AnnouncementsPage from './alumni/announcementsPage';
import PasswordPage from './alumni/passwordPage';

export const HomePage = () => {
  return (
    <Router>
      <Header />
      <AlumniSidebar />
      <div className=" content-wrapper">
        <Switch>
          <Route exact path="/dashboard">
            <DashboardPage />
          </Route>
          <Route exact path="/available_posts">
            <AvailablePostsPage />
          </Route>
          <Route exact path="/results">
            <ResultsPage />
          </Route>
          <Route exact path="/profile">
            <ProfilePage />
          </Route>
          <Route exact path="/cv">
            <CvPage />
          </Route>
          <Route exact path="/projects">
            <ProjectsPage />
          </Route>
          <Route exact path="/chat_page">
            <ChatPage />
          </Route>
          <Route exact path="/announcements">
            <AnnouncementsPage />
          </Route>
          <Route exact path="/password">
            <PasswordPage />
          </Route>
        </Switch>
    </div>
    </Router>
    );
  }

