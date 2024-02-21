import { useState, useEffect } from 'react';
import { Link, Outlet } from 'react-router-dom';
import { Header, HeaderContainer, HeaderGlobalBar, HeaderName, HeaderGlobalAction, SkipToContent, HeaderMenuButton, Theme, HeaderPanel, SideNav, SideNavLink, SideNavItems } from "@carbon/react";
import {UserAvatarFilledAlt, Events, BrightnessContrast, Logout, Login, Report, IbmTelehealth, IbmWatsonSpeechToText, Category} from '@carbon/icons-react';

export default function NavBar({setTheme}) {
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
                            <Link renderIcon={Logout}>Logout</Link>
                        </HeaderPanel>
                    </Header>
                    <SideNav expanded={isSideNavExpanded} aria-label="Side navigation" onSideNavBlur={onClickSideNavExpand} isPersistent={false} href="#main-content">
                        <SideNavItems>
                            <SideNavLink renderIcon={Report} href="/report-summary">Report summary</SideNavLink>
                            <SideNavLink renderIcon={IbmTelehealth} href='/doctors'>Doctors</SideNavLink>
                            <SideNavLink renderIcon={IbmWatsonSpeechToText} href='patient-transcript'>Patient transcript</SideNavLink>
                            <SideNavLink renderIcon={Category} href='/disease-categorizer'>Disease categorizer</SideNavLink>
                            <SideNavLink renderIcon={Events} href="about-us">About us</SideNavLink>
                        </SideNavItems>
                    </SideNav>
                </Theme>
                <Outlet/>
            </>
        )} />
    )
}