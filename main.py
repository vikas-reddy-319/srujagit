import streamlit as st
def main(): 
    html_temp="""
     <div style = "background-color:lightblue;padding:16px">
     <h2 style="color:black;text-align:center;"> Car Price Prediction Using ML</h2>
     </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
   
    st.markdown("##### Are you planning to sell your car !?\n##### So let's try evaluating the price..")
    
    st.write('')
    st.write('')
    test_slider = st.slider('Test Slider', 0, 100, 50)
    st.write(f'Selected value: {test_slider}')
  
if __name__ == '__main__':
    main()
