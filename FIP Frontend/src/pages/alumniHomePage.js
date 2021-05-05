import React from 'react';
import { BrowserRouter as Router, Switch, Route, Link, useRouteMatch } from 'react-router-dom';
import { DashboardPage } from './alumni/dashboardPage';
import AvailablePostsPage from './alumni/availablePosts';
import ResultsPage from './alumni/resultsPage';
import ProfilePage from './alumni/profilePage';
import CvPage from './alumni/cvPage';
import ProjectsPage from './alumni/projectsPage';
import ChatPage from './alumni/chatPage';
import AnnouncementsPage from './alumni/announcementsPage';
import PasswordPage from './alumni/passwordPage';


export const AlumniHomePage = () => {

    return (
        <Router>
      <aside className="main-sidebar">
          <section className="sidebar">
              <div className="user-panel">
                  <div className="pull-left image">
                      <img src="img/timo.jpg" className="img-circle" alt="User Image" />
                  </div>
                  <div className="pull-left info">
                      <p>t-m@re</p>
              <a href="#"><i className="fa fa-circle text-success"></i> Online</a>
              </div>
              </div>
              <ul className="sidebar-menu" data-widget="tree">
                  <li className="header">ALUMNI NAVIGATION</li>
                  <li>
                  <Link to = "/dashboard">
                      <i className="fa fa-th"></i> <span>Dashboard</span>
                  </Link>
                  </li>
                  <li>
                  <Link to = "/available_posts">
                      <i className="fa fa-th"></i> <span>View Available Posts</span>
                  </Link>
                  </li>
                  <li>
                  <Link to = "/results">
                      <i className="fa fa-th"></i> <span>View Results</span>
                  </Link>
                  </li>
                  <li className="treeview">
                      <a href="#">
                          <i className="fa fa-files-o"></i>
                        <span>My Account</span>
                        <span className="pull-right-container">
                      <small className="label pull-right bg-green">new</small>
                      </span>
                      </a>
                      <ul className="treeview-menu">
                          <li><Link to = "/profile" className = "Hover" ><i className="fa fa-circle-o"></i> Profile</Link></li>
                          <li><Link to ="/cv"><i className="fa fa-circle-o"></i> My Cv</Link></li>
                          <li><Link to ="/projects"><i className="fa fa-circle-o"></i> My Projects</Link></li>
                      </ul>
                  </li>
                  <li>
                  <Link to = "/chat_page">
                      <i className="fa fa-th"></i> <span>Chat Room</span>
                  </Link>
                  </li>
                  <li>
                  <Link to = "/announcements">
                      <i className="fa fa-th"></i> <span>Announcements</span>
                  </Link>
                  </li>
                  <li>
                  <Link to = "/password">
                      <i className="fa fa-th"></i> <span>Change Password</span>
                      
                  </Link>
                  </li>
              </ul>
          </section>
        </aside>
        <div className=" content-wrapper">
        <Switch>
          <Route exact path={["/dashboard", "/"]}>
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

