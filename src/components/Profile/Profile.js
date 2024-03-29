import { Breadcrumb, BreadcrumbItem, Column, FlexGrid, Grid, Row, Stack, Tag, TextInput } from "@carbon/react";
import { CheckmarkFilled} from '@carbon/icons-react';
import {FirstAid, SocialWork_02} from '@carbon/pictograms-react';
import backgroundImage from './syringe-1884784_1280.jpg'
export default function Profile() {
    return(
        <div className="profile-padding">
            <div style={{backgroundColor:'rgba(256 , 256,256,0.5)'}}>
            <h3 style={{padding:'2rem',color:'black'}}>My Profile</h3>
            <Grid>
                <Column lg={8} className="column1">
                    <Stack gap={7}>
                    <Grid>
                        <Column sm={4}>
                            <TextInput style={{color:'black'}} labelText='First name' value='Alston' readOnly />
                        </Column>
                        <Column sm={4}>
                            <TextInput style={{color:'black'}} labelText='Last name' value='Dias' readOnly />
                        </Column>
                    </Grid>
                    <TextInput style={{color:'black'}} labelText='Address' value='Margao, South Goa, India' readOnly />
                    <TextInput style={{color:'black'}} labelText='Phone Number' value='7872638862' readOnly />
                    <TextInput style={{color:'black'}} labelText='Email ID' value='alston_dias@gmail.com' readOnly />
                    </Stack>
                </Column>
                <Column span={8} >
                    <Grid>
                        <Column span={4} className="column2">
                        <div style={{display:'inline-flex', padding:'1rem'}}>
                        <div><FirstAid className="firstaid"/></div>
                        <div style={{paddingInlineStart:'1rem', display:'grid', alignContent:'center'}}>
                            <Tag type="red" size="md" renderIcon={CheckmarkFilled}>{"Patient id"}</Tag>
                            <div><h3>1289</h3></div>
                        </div>
                    </div>
                        </Column>
                    </Grid>
                    {/*
                    <Grid>
                        <Column span={4} style={{padding:'3rem'}}>
                            <img style={{width:'300px'}} src={'/images/ehr-1476525_1280.png'}/>
                        </Column>
                    </Grid>
                    */}
                </Column>   
            </Grid>
            </div>
        </div>
    )
}