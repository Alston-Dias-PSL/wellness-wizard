import { useState, useEffect } from 'react';
import { NavLink, Outlet } from 'react-router-dom';
import { Link, Header, HeaderContainer, HeaderGlobalBar, HeaderName, HeaderGlobalAction, SkipToContent, HeaderMenuButton, Theme, HeaderPanel, SideNav, SideNavLink, SideNavItems } from "@carbon/react";
import {UserAvatarFilledAlt, Events, BrightnessContrast, Logout, Login, Report, IbmTelehealth, IbmWatsonSpeechToText, Category, FaceMask, PillsAdd} from '@carbon/icons-react';

export default function NavBar({cookies, setCookie, removeCookie, setTheme}) {
    const [isProfileExpanded, setIsProfileExpanded] = useState(false);
    const [navbarMode, setNavbarMode] = useState('g90');
    const [isLogin, setIsLogin] = useState(true);

    return(
        <HeaderContainer render={({ isSideNavExpanded, onClickSideNavExpand }) => (
            <>
                <Theme theme={navbarMode}>
                    <Header aria-label='Wellness Wizard'>
                        <SkipToContent />
                        <HeaderMenuButton aria-label={isSideNavExpanded ? 'Close menu' : 'Open menu'} onClick={onClickSideNavExpand} isActive={isSideNavExpanded} isCollapsible />
                        <HeaderName href="/" prefix="IBM" isCurrentPage>Wellness Wizard</HeaderName>
                        <HeaderGlobalBar>
                            <HeaderGlobalAction aria-label="change theme" onClick={setTheme} >
                                <BrightnessContrast size={25}/>
                            </HeaderGlobalAction>
                            <HeaderGlobalAction
                            aria-label='user'
                            onClick={()=>setIsProfileExpanded(!isProfileExpanded)} 
                            id="profile-switcher"
                            >
                                <UserAvatarFilledAlt size={25} />
                            </HeaderGlobalAction>
                        </HeaderGlobalBar>
                        <HeaderPanel expanded={isProfileExpanded}>
                            <h4 style={{paddingBottom:'1rem'}}>User name</h4>
                            <NavLink style={{alignItems:'center', display:'flex'}} className='Link-style-color' to='/profile'>Go to my profile &nbsp;<FaceMask/> </NavLink>
                            <div>
                            <Link href='#' size='lg' className='logout-button' renderIcon={Login}>Login</Link>
                            </div>
                        </HeaderPanel>
                    </Header>
                    <SideNav expanded={isSideNavExpanded} aria-label="Side navigation" onSideNavBlur={onClickSideNavExpand} isPersistent={false} href="#main-content">
                        <SideNavItems>
                            <SideNavLink renderIcon={Report}><NavLink className='Link-style' to='/report-summary'>Report summary</NavLink></SideNavLink>
                            <SideNavLink renderIcon={IbmTelehealth}><NavLink className='Link-style' to='/doctors'>Doctors</NavLink></SideNavLink>
                            <SideNavLink renderIcon={IbmWatsonSpeechToText}><NavLink  className='Link-style' to='/patient-transcript'>Patient transcript</NavLink></SideNavLink>
                            <SideNavLink renderIcon={Category}><NavLink className='Link-style' to='/disease-categorizer'>Disease categorizer</NavLink></SideNavLink>
                            <SideNavLink renderIcon={Events} ><NavLink className='Link-style' to='/about-us'>About us</NavLink></SideNavLink>
                            <SideNavLink renderIcon={PillsAdd} ><NavLink className='Link-style' to='/medicine-stock'>Medicine stock</NavLink></SideNavLink>
                        </SideNavItems>
                    </SideNav>
                </Theme>
                <Outlet/>
            </>
        )} />
    )
}