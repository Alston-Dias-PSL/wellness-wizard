import { FlexGrid, Row, Column } from '@carbon/react';
import { LineChart, ExperimentalChoroplethChart } from '@carbon/charts-react'
import data from './data.js';
import options from './options.js';
import geooptions from './geooptions.js';
import geodata from './geodata.js';
import '@carbon/charts-react/styles.css'

export default function MedicineStock () {
    return(
        <div className='medicine-padding'>
            <h3>Medicine Stock</h3>
            <FlexGrid>
                <Row>
                    <Column lg={8}>
                    <LineChart data={data} options={options} />
                    </Column>
                    <Column lg={8}>
                    {/*<ExperimentalChoroplethChart data={geodata} options={geooptions}/>*/}
                    </Column>
                </Row>
            </FlexGrid>
        </div>
    )
}