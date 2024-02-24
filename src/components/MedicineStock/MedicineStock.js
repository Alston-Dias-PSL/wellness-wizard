import { FlexGrid, Row, Column } from '@carbon/react';
import { LineChart, ExperimentalChoroplethChart } from '@carbon/charts-react'
import data from './data.js';
import options from './options.js';
import geooptions from './geooptions.js';
import geodata from './geodata.js';
import '@carbon/charts-react/styles.css'
import ChatBot from '../ChatBot/ChatBot.js';

export default function MedicineStock () {
    return(
        <div className='medicine-padding'>
            <h3>Medicine Stock</h3> 
            <p className='medicine-description'>on medicine stock availaibility across hospitals,
            ensuring vital supplies are readily accessible. Explore which areas have procured
            specific medications, aiding in targated distribution and efficient healthcare management.
            Discover real-time updates</p>
            <FlexGrid>
                <Row>
                    <Column lg={8}>
                    <LineChart data={data} options={options} />
                    </Column>
                    <Column lg={8}>
                        <ExperimentalChoroplethChart data={geodata} options={geooptions}/>
                    </Column>
                </Row>
            </FlexGrid>
            <ChatBot/>
        </div>
    )
}