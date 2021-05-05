import React from 'react';
import { BrowserRouter as Router, Switch, Route, Link, useRouteMatch } from 'react-router-dom';
import { DashboardPage } from './student/dashboardPage';
import AvailablePostsPage from './student/availablePosts';
import ProfilePage from './student/profilePage';
import ProjectsPage from './student/projectsPage';
import PasswordPage from './student/passwordPage';


export const StudentHomePage = () => {

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
                  <li className="header">STUDENT NAVIGATION</li>
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
                          <li><Link to ="projects"><i className="fa fa-circle-o"></i> My Projects</Link></li>
                      </ul>
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
          <Route exact path="/profile">
            <ProfilePage />
          </Route>
          <Route exact path="/projects">
            <ProjectsPage />
          </Route>
          <Route exact path="/password">
            <PasswordPage />
          </Route>
        </Switch>
            </div>
    </Router>
    );
  }

