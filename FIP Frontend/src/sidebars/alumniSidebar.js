import React, { Component } from 'react';
import { BrowserRouter as Router, Switch , Route, Link, useRouteMatch } from 'react-router-dom';

export const AlumniSidebar = () => {
    let { path, url } = useRouteMatch();

    return (

      <div>
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
                  <li className="header">MAIN NAVIGATION</li>
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
                          <li><Link to ="projects"><i className="fa fa-circle-o"></i> My Projects</Link></li>
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
      </div>
    );
  }

