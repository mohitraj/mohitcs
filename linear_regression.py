'''
In order to calculate linear regression
y =a+bx

b = cov(x,y)/var(x)


'''

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class stats:

    def __init__(self):
        pass

    def get_data(self,file_name,*fields):
        data_list = []
        data = pd.read_csv(file_name)
        for each in fields:
            data_list.append(list(data.get(each)))
        return data_list

    def list_to_array(self,values):
        np_array = np.array(values)
        return np_array
    def get_mean(self,values):
        return np.mean(values)


    def get_std(self,values):
        return np.std(values)

    def variance(self,num_array):
        return np.var(num_array, ddof=1)

    def covariance(self,X_array,Y_array):
        return np.cov(X_array, Y_array)[0][1]

    def independent_variables(self,*var):
        a = np.array(var)
        return a.T


    def array_to_reg(self,array):
        np_array = self.list_to_array(array)
        return self.array_to_reg(np_array)

    def correlation(self,x,y):
        x= np.array(x)
        y=np.array(y)
        return np.corrcoef([x,y])[0][1]

    def correlation_multiple(self,*var):
        corr_result=[]
        return np.corrcoef(var)






class Linear_Regression(stats):
    def __init__(self):
        pass

    def beta_coff(self,x_array,y_array):
        cov1 = self.covariance(x_array,y_array)
        var1 = self.variance(x_array)
        b= cov1/var1
        return b
    def intercept(self,x_array,y_array):
        x_mean = self.get_mean(x_array)
        y_mean = self.get_mean(y_array)
        beta = self.beta_coff(x_array,y_array)
        return y_mean- beta*x_mean

    def R_squared(self,x_tain,y_train,x_test,y_test):
        model = LinearRegression()
        model.fit(x_tain,y_train)
        return model.score(x_test, y_test)

    def predicted(self,x_train,y_train,x_test):
        model = LinearRegression()
        model.fit(x_train, y_train)
        return  model.predict(x_test)





    def plot1(self,X_sc,Y_sc,x_data,y_data):
        plt.axis([0, 25, 0, 25])
        plt.grid(True)
        plt.scatter(X_sc, Y_sc)
        plt.plot(x_data,y_data, c='r', linestyle='--')
        plt.show()

class hypo_test(stats):
    def __init__(self):
        pass
    #when the sample size is more than 30
    def z_score_cal(self, sample_mean,population_mean,pop_s_d, sample_size):
        a = (sample_mean-population_mean)
        b = pop_s_d/math.sqrt(sample_size  )
        z = a/float(b)
        return z

    def p_values_z_test(self,z_score):
        p_values = 1-scipy.stats.norm.sf(abs(z_score))
        return p_values

obj1 = Linear_Regression()

diameter =[6, 8, 10, 14, 18]  # replace it
topping = [2,1,0,2,0]
price = [7, 9, 13, 17.5, 18]

independent_var = obj1.independent_variables(diameter,topping)



diameter_test = [8,9,11,16,12]
topping_test = [2,0,2,2,0]

independent_var_test = obj1.independent_variables(diameter_test,topping_test)
print obj1.predicted(independent_var,price,independent_var_test)



price_test = [11,8.5,15,18,11]
#print obj1.list_to_array(X_test)



#print obj1.plot1(independent_var,obj1.list_to_array(price),obj1.list_to_array(price_test),obj1.predicted(independent_var,price,independent_var_test),)
#print obj1.correlation_multiple( X_values, Y_values,X_test)