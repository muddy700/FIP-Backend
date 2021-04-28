import React from 'react';
import { Link } from 'react-router-dom';

export const Header = () => {
        return (
            <header className="main-header">
                <a href="#" className="logo">
                    <span className="logo-mini"><b>A</b>LT</span>
                    <span className="logo-lg"><b>Admin</b>LTE</span>
                </a>
                <nav className="navbar navbar-static-top">
                    <a href="#" className="sidebar-toggle" data-toggle="push-menu" role="button">
                        <span className="sr-only">Toggle navigation</span>
                    </a>
                    <div className="navbar-custom-menu">
                        <ul className="nav navbar-nav">

                        <Link to = "/"><button className="btn btn-success" type='button' style={{ width: "70px" }} >Log Out </button></Link>


                            <li className="dropdown messages-menu">
                                <a href="#" className="dropdown-toggle" data-toggle="dropdown">
                                    <i className="fa fa-envelope-o"></i>
                                    <span className="label label-success">support</span>
                                </a>
                                <ul className="dropdown-menu">
                                    <li className="header">t-m@re: Registration System</li>
                                    <li>
                                        <ul className="menu">
                                            <li>
                                                <a href="#">
                                                    <div className="pull-left">
                                                    <img src="img/timo.jpg" className="img-circle" alt="User Image" />
                                                    </div>
                                                    <h4>
                                                      t-m@re: Support Team
                                                        <small><i className="fa fa-clock-o"></i> 5 mins</small>
                                                    </h4>
                                                    <p> welcome to t-m@re System?</p>
                                                    <p> +255765281000</p>
                                                    <p>  timotheomhoja@gmail.com</p>
                                                </a>
                                            </li>
                                        </ul>
                                    </li>
                                </ul>
                            </li>
                        </ul>
                    </div>
                </nav>
            </header>
        )
    }

